import collections
import itertools
import math

DELTA = 1e-5

def argmin(L):
  return min(enumerate(L), key=lambda x: x[1])[0]

def unroll(f):
  """Returns g such that g(x) = f(*x)."""
  return lambda x: f(*x)

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
    Player = collections.namedtuple('Player', ['z'])
    self.graph = Graph([(0, 1)])
    self.strategies = values
    self.players = [Player(player_val) for player_val in players]

  def cost(self, strategy_index, z, neigbor_strategies):
    """
    Args:
      strategy_index - index of s_i
      z - index of z_i
      adjacent_strategies - collection of surrounding s_j.
    """
    dist_to_self = self.dist(z, strategy_index)**2
    dist_to_neighbors = sum(map(
        lambda neighbor_strategy: self.dist(neighbor_strategy, strategy_index)**2,
        neigbor_strategies))
    return dist_to_self + dist_to_neighbors

  def dist(self, strategy1, strategy2):
    """distance from self.values[i] to self.values[j]."""
    return abs(self.strategies[strategy1] - self.strategies[strategy2])

  def adj(self, i):
    """List of players adjacent to i."""
    return [j for j in range(len(self.players))
          if self.graph.contains((i, j)) and i != j]
  
  def update(self):
    self.cost_matrix = {}  # (tuple of player values) -> (tuple of payoffs)
    for values_idx in itertools.product(  # |players| copies of self.strategies
      range(len(self.strategies)), repeat=len(self.players)):
      costs = []
      for i in range(len(self.players)):
         cost_to_i = self.cost(
           values_idx[i], self.players[i].z, [values_idx[j] for j in self.adj(i)])
         costs.append(cost_to_i)
      self.cost_matrix[values_idx] = costs
          
  def deviations(self, strategy_tuple, i):
    """Generates deviations for player i."""
    deviation = list(strategy_tuple)
    for dev in range(len(self.strategies)):
      if dev != strategy_tuple[i]:
        deviation[i] = dev
        yield tuple(deviation)

  def is_equilibrium(self, values_idx, comp=lambda x,y: y-x>DELTA):
    for player in range(len(self.players)):
      for deviation in self.deviations(values_idx, player):
        if comp(
          self.cost_matrix.get(deviation)[player],
          self.cost_matrix.get(values_idx)[player]):
          return False
    return True

  def get_equilibria(self):
    equilibria = []
    for values_idx in self.cost_matrix.keys():
      if self.is_equilibrium(values_idx):
        equilibria.append(values_idx)
    return equilibria

## Tests
def testBasicGetEquilibria():
  G = Game(values=[.125 * i for i in range(9)], players=[0, 8])
  G.update()
  equilibria = G.get_equilibria()
  assert(len(equilibria) == 3)
  for tup in ((2, 5), (3, 6), (3, 5)):
    assert(tup in equilibria)
  return G

_G = testBasicGetEquilibria()
           
##        for i, player in enumerate(self.players):
##            S = [self.players[j].s
##                 for j in range(len(self.players))
##                 if self.graph.contains((i, j))]  # All surrounding value indices
##            min_idx = argmin(self.cost(idx, player.z, S)
##                             for idx in range(len(self.values)))
##            for j, val in enumerate(self.values):
##                print("Cost to", i, "of", val, "is", self.cost(j, player.z, S))
##            print("Min value for player", i, "is", self.values[min_idx])
            
            
