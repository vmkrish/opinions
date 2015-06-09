Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
testBasicGetEquilibria: equilibria are [(0.375, 0.75), (0.375, 0.625), (0.25, 0.625)]
>>> G = EuclideanPartitionGame(
    graph=Graph([(0, 1)]),
    values=[1, 2, 3, 4],
    num_players=2)
>>> G.strategies
[{(1, 2, 3, 4)}, {(2, 3, 4), (1,)}, {(2,), (1, 3, 4)}, {(1, 2), (3, 4)}, {(2,), (3, 4), (1,)}, {(3,), (1, 2, 4)}, {(1, 3), (2, 4)}, {(3,), (2, 4), (1,)}, {(2, 3), (1, 4)}, {(2,), (3,), (1, 4)}, {(1, 2, 3), (4,)}, {(2, 3), (1,), (4,)}, {(2,), (1, 3), (4,)}, {(1, 2), (3,), (4,)}, {(2,), (3,), (1,), (4,)}]
>>> G.get_alpha(G.strategies[0])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    G.get_alpha(G.strategies[0])
  File "C:\Users\Viknesh\Desktop\opinions\research.py", line 123, in get_alpha
    self.alphas[dev] = - (dist_btwn_strategy - dist_btwn_dev) / (dist_to_strategy - dist_to_dev)
ZeroDivisionError: float division by zero
>>> for i in range(100:
	       
SyntaxError: invalid syntax
>>> for i in range(10):
	if i == 1:
		pass
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> ================================ RESTART ================================
>>> 
testBasicGetEquilibria: equilibria are [(0.375, 0.75), (0.375, 0.625), (0.25, 0.625)]
>>> G = EuclideanPartitionGame(
    graph=Graph([(0, 1)]),
    values=[1, 2, 3, 4],
    num_players=2)
>>> G.get_alpha(G.strategies[0])
{{(2,), (3, 4), (1,)}: 1.125, {(2,), (3,), (1,), (4,)}: 1.0, {(3,), (2, 4), (1,)}: 1.1666666666666667, {(3,), (1, 2, 4)}: 2.0, {(2,), (1, 3), (4,)}: 1.1666666666666667, {(2,), (3,), (1, 4)}: 1.5, {(2,), (1, 3, 4)}: 2.0, {(2, 3), (1,), (4,)}: 1.0, {(1, 2), (3,), (4,)}: 1.125, {(1, 3), (2, 4)}: 2.0, {(2, 3), (1, 4)}: 2.0, {(2, 3, 4), (1,)}: 1.2857142857142856, {(1, 2, 3), (4,)}: 1.2857142857142856, {(1, 2), (3, 4)}: 1.3333333333333333}
>>> min(G.get_alpha(G.strategies[0]).values())
1.0
>>> for strategy in G.strategies:
	print(min(G.get_alpha(strategy).values()))

	
1.0
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    print(min(G.get_alpha(strategy).values()))
  File "C:\Users\Viknesh\Desktop\opinions\research.py", line 124, in get_alpha
    self.alphas[dev] = - (dist_btwn_strategy - dist_btwn_dev) / (dist_to_strategy - dist_to_dev)
ZeroDivisionError: float division by zero
>>> ================================ RESTART ================================
>>> 
testBasicGetEquilibria: equilibria are [(0.375, 0.75), (0.375, 0.625), (0.25, 0.625)]
>>> G = EuclideanPartitionGame(
    graph=Graph([(0, 1)]),
    values=[1, 2, 3, 4],
    num_players=2)
>>> for strategy in G.strategies:
	print(min(G.get_alpha(strategy).values()))

	
1.0
{(1, 2, 3, 4)} approximately equal to {(2, 3, 4), (1,)} !
{(2,), (1, 3, 4)} approximately equal to {(2, 3, 4), (1,)} !
{(3,), (1, 2, 4)} approximately equal to {(2, 3, 4), (1,)} !
{(1, 3), (2, 4)} approximately equal to {(2, 3, 4), (1,)} !
{(2, 3), (1, 4)} approximately equal to {(2, 3, 4), (1,)} !
{(2,), (3,), (1, 4)} approximately equal to {(2, 3, 4), (1,)} !
Traceback (most recent call last):
  File "<pyshell#17>", line 2, in <module>
    print(min(G.get_alpha(strategy).values()))
  File "C:\Users\Viknesh\Desktop\opinions\research.py", line 126, in get_alpha
    self.alphas[dev] = - (dist_btwn_strategy - dist_btwn_dev) / (dist_to_strategy - dist_to_dev)
ZeroDivisionError: float division by zero
>>> ================================ RESTART ================================
>>> 
testBasicGetEquilibria: equilibria are [(0.375, 0.75), (0.375, 0.625), (0.25, 0.625)]
>>> G = EuclideanPartitionGame(
    graph=Graph([(0, 1)]),
    values=[1, 2, 3, 4],
    num_players=2)
>>> for strategy in G.strategies:
	print(min(G.get_alpha(strategy).values()))

	
1.0
{(1, 2, 3, 4)} approximately equal to {(2, 3, 4), (1,)} !
{(2,), (1, 3, 4)} approximately equal to {(2, 3, 4), (1,)} !
{(3,), (1, 2, 4)} approximately equal to {(2, 3, 4), (1,)} !
{(1, 3), (2, 4)} approximately equal to {(2, 3, 4), (1,)} !
{(2, 3), (1, 4)} approximately equal to {(2, 3, 4), (1,)} !
{(2,), (3,), (1, 4)} approximately equal to {(2, 3, 4), (1,)} !
{(1, 2, 3), (4,)} equal to {(2, 3, 4), (1,)} !!
Traceback (most recent call last):
  File "<pyshell#20>", line 2, in <module>
    print(min(G.get_alpha(strategy).values()))
  File "C:\Users\Viknesh\Desktop\opinions\research.py", line 128, in get_alpha
    self.alphas[dev] = - (dist_btwn_strategy - dist_btwn_dev) / (dist_to_strategy - dist_to_dev)
ZeroDivisionError: float division by zero
>>> ================================ RESTART ================================
>>> 
testBasicGetEquilibria: equilibria are [(0.375, 0.75), (0.375, 0.625), (0.25, 0.625)]
>>> G = EuclideanPartitionGame(
    graph=Graph([(0, 1)]),
    values=[1, 2, 3, 4],
    num_players=2)
>>> for strategy in G.strategies:
	print(min(G.get_alpha(strategy).values()))

	
1.0
-2.9999999999999987
0.0
-0.7500000000000002
-0.5
0.0
INFO: {(2, 3), (1, 4)} is equivalent to {(1, 3), (2, 4)} .
0.0
FATAL: {(1, 2, 3, 4)} is a better response to {(3,), (2, 4), (1,)} !
FATAL: {(1, 3), (2, 4)} is a better response to {(3,), (2, 4), (1,)} !
FATAL: {(2, 3), (1, 4)} is a better response to {(3,), (2, 4), (1,)} !
-0.7500000000000002
INFO: {(1, 3), (2, 4)} is equivalent to {(2, 3), (1, 4)} .
0.0
FATAL: {(1, 2, 3, 4)} is a better response to {(2,), (3,), (1, 4)} !
FATAL: {(1, 3), (2, 4)} is a better response to {(2,), (3,), (1, 4)} !
FATAL: {(2, 3), (1, 4)} is a better response to {(2,), (3,), (1, 4)} !
0.0
-2.9999999999999987
FATAL: {(1, 2, 3, 4)} is a better response to {(2, 3), (1,), (4,)} !
FATAL: {(1, 3), (2, 4)} is a better response to {(2, 3), (1,), (4,)} !
FATAL: {(2, 3), (1, 4)} is a better response to {(2, 3), (1,), (4,)} !
-0.5
FATAL: {(1, 2, 3, 4)} is a better response to {(2,), (1, 3), (4,)} !
FATAL: {(1, 3), (2, 4)} is a better response to {(2,), (1, 3), (4,)} !
FATAL: {(2, 3), (1, 4)} is a better response to {(2,), (1, 3), (4,)} !
-0.7500000000000002
-0.5
0.0
>>> x = HashablePartition({(3,), (2, 4), (1,)})
>>> y = HashablePartition({(1, 2, 3, 4)})
>>> G.dist_to_player(0, y)
1.25
>>> G.dist_to_player(0, x)
0.5
>>> G.dist_(x, x)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    G.dist_(x, x)
AttributeError: 'EuclideanPartitionGame' object has no attribute 'dist_'
>>> G.dist(x, x)
1.0
>>> G.dist(y, y)
0.0
>>> G.dist(x, y)
0.875
>>> G.dist(y, x)
0.875
>>> 
