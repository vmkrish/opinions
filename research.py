import collections
import itertools
import math

DELTA = 1e-5

def argmin(L):
  return min(enumerate(L), key=lambda x: x[1])[0]

def partition(L):
  """Yields sets of tuples."""
  if not L:
    yield set()
  for i in range(int(2**(len(L)-1))):
    parts = (list(), list())
    for item in L:
      parts[i%2].append(item)
      i >>= 1
    for rest in partition(parts[1]):
      
      yield {tuple(parts[0])} | rest

class HashablePartition(set):
  def __hash__(self):
    _list = list(self)
    _list.sort()
    return tuple(_list).__hash__()

def unroll(f):
  """Returns g such that g(x) = f(*x)."""
  return lambda x: f(*x)

class Player(collections.namedtuple('Player', ['z'])):
  pass

class Graph(object):
  def __init__(self, L=()):
    """L is an optional list of tuples of graph edges.
    eg, L = [(0, 1), (1, 2)]"""
    self.adjacencies = collections.defaultdict(bool)
    for i in L:
      self.insert(i)
  def insert(self, pair):
    pair_ = pair if pair < pair[::-1] else pair[::-1]
    self.adjacencies[pair_] = True
  def contains(self, pair):
    pair_ = pair if pair < pair[::-1] else pair[::-1]
    return pair_ in self.adjacencies

        
class Game(object):
  def __init__(self, graph=None, values=None, players=None):
    """
    Args:
      graph: List of edges between players, eg
        [(0, 1), (1, 2), (0, 2)].
      values: A list to use for the values set.
      players: List of player z initial values indicies, eg
        [0, 1, 2].  Should be same size as graph.
    """
    self.graph = graph
    self.strategies = values
    self.players = [Player(player_val) for player_val in players]

  def cost(self, strategy, z, neigbor_strategies):
    """Cost of playing strategy if internal value is z.

    Args:
      strategy - ith player's strategy
      z - index of z_i
      adjacent_strategies - collection of surrounding s_j.
    """
    dist_to_self = self.dist(z, strategy)
    dist_to_neighbors = sum(map(
        lambda neighbor_strategy: self.dist(neighbor_strategy, strategy),
        neigbor_strategies))
    return dist_to_self + dist_to_neighbors

  def dist(self, strategy1, strategy2):
    """distance from strategy1 to strategy2."""
    return abs(strategy1 - strategy2)**2

  def adj(self, i):
    """List of players adjacent to i."""
    return [j for j in range(len(self.players))
          if self.graph.contains((i, j)) and i != j]
  
  def update(self):
    self.cost_matrix = {}  # (tuple of player values) -> (tuple of payoffs)
    for all_players_strategies in itertools.product(  # |players| copies of self.strategies
      self.strategies, repeat=len(self.players)):
      costs = []
      for i in range(len(self.players)):
         cost_to_i = self.cost(
           all_players_strategies[i],
           self.strategies[self.players[i].z],
           [all_players_strategies[j] for j in self.adj(i)])
         costs.append(cost_to_i)
      self.cost_matrix[all_players_strategies] = costs
          
  def deviations(self, strategy_tuple, i):
    """Generates deviations for player i."""
    deviation = list(strategy_tuple)
    for dev in self.strategies:
      if dev != strategy_tuple[i]:
        deviation[i] = dev
        yield tuple(deviation)

  def is_equilibrium(self, all_players_strategies, comp=lambda x,y: y-x>DELTA):
    for player in range(len(self.players)):
      for deviation in self.deviations(all_players_strategies, player):
        if comp(
          self.cost_matrix.get(deviation)[player],
          self.cost_matrix.get(all_players_strategies)[player]):
          return False
    return True

  def get_equilibria(self):
    equilibria = []
    for all_players_strategies in self.cost_matrix.keys():
      if self.is_equilibrium(all_players_strategies):
        equilibria.append(all_players_strategies)
    return equilibria

class PartitionGame(Game):
  def __init__(self, graph=None, values=None, players=None):
    """
    Args:
      graph: List of edges between players, eg
        [(0, 1), (1, 2), (0, 2)].
      values: A list to use for the values set.
      players: List of player z initial values indicies, eg
        [0, 1, 2].  Should be same size as graph.
    """
    super().__init__(
      graph=graph, values=values, players=players)
    self.strategies = [HashablePartition(p) for p in partition(values)]
    self.num_values = len(values)

  @classmethod
  def GetRelevantTupleFromPartition(cls, z, partition):
    """Returns the set t such that z in t and t in partition."""
    for t in partition:
      if z in t:
        return set(t)
    
  def dist(self, strategy1, strategy2):
    """distance from strategy1 to strategy2."""
    return 1 - len(set.intersection(strategy1, strategy2))/max(len(strategy1), len(strategy2))
  
  def cost(self, strategy_index, z, neigbor_strategies):
    """
    Args:
      strategy_index - index of s_i
      z - z value (not index!)
      adjacent_strategies - collection of surrounding s_j.
    """
    dist_to_self = self.dist(z, strategy_index)
    dist_to_neighbors = sum(map(
        lambda neighbor_strategy: self.dist(neighbor_strategy, strategy_index),
        neigbor_strategies))
    return dist_to_self + dist_to_neighbors

## Tests
def testBasicGetEquilibria():
  G = Game(
    graph=Graph([(0, 1)]),  # player[0] connected to player[1]
    values=[.125 * i for i in range(9)],
    players=[0, 8])
  G.update()
  equilibria = G.get_equilibria()
  assert(len(equilibria) == 3)
  for tup in ((0.375, 0.75), (0.375, 0.625), (0.25, 0.625)):
    assert(tup in equilibria)
  print("testBasicGetEquilibria: equilibria are", equilibria)
  return G

def testBasicPartitionGame():
  PG = PartitionGame(
    graph=Graph([(0, 1)]),
    values=[1, 2, 3, 4],
    players=[0, 3])
  return PG

TESTS = [testBasicGetEquilibria, testBasicPartitionGame]
RESULTS = []

if __name__ == '__main__':
  for test in TESTS:
    RESULTS.append(test())
  assert(all(RESULTS))
  _G = RESULTS[TESTS.index(testBasicGetEquilibria)]
  _PG = RESULTS[TESTS.index(testBasicPartitionGame)]
           
##        for i, player in enumerate(self.players):
##            S = [self.players[j].s
##                 for j in range(len(self.players))
##                 if self.graph.contains((i, j))]  # All surrounding value indices
##            min_idx = argmin(self.cost(idx, player.z, S)
##                             for idx in range(len(self.values)))
##            for j, val in enumerate(self.values):
##                print("Cost to", i, "of", val, "is", self.cost(j, player.z, S))
##            print("Min value for player", i, "is", self.values[min_idx])
            
            
