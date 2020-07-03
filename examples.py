"""Example runs with Little Ball of Fur."""

import networkx as nx
import matplotlib.pyplot as plt

from littleballoffur.dataset import GraphReader

from littleballoffur.node_sampling import RandomNodeSampler, DegreeBasedSampler, PageRankBasedSampler

from littleballoffur.exploration_sampling import CommunityStructureExpansionSampler, CirculatedNeighborsRandomWalkSampler
from littleballoffur.exploration_sampling import LoopErasedRandomWalkSampler, BreadthFirstSearchSampler, DepthFirstSearchSampler, SnowBallSampler
from littleballoffur.exploration_sampling import RandomWalkSampler, RandomNodeNeighborSampler, MetropolisHastingsRandomWalkSampler
from littleballoffur.exploration_sampling import ShortestPathSampler, CommonNeighborAwareRandomWalkSampler, NonBackTrackingRandomWalkSampler
from littleballoffur.exploration_sampling import RandomWalkWithRestartSampler, RandomWalkWithJumpSampler, FrontierSampler, ForestFireSampler

from littleballoffur.edge_sampling import RandomEdgeSamplerWithPartialInduction
from littleballoffur.edge_sampling import RandomEdgeSampler, RandomNodeEdgeSampler, HybridNodeEdgeSampler, RandomEdgeSamplerWithInduction

reader = GraphReader("facebook")

graph = reader.get_graph()
# #画图
# pos = nx.spring_layout(graph)
# #nx.draw_spring(graph, node_size=15, node_color=node_lable, cmap=plt.get_cmap('hsv'), with_labels = True )
# plt.figure(1)
# nx.draw(graph, node_size=20, cmap=plt.get_cmap('hsv'), with_labels = True, font_size = 6, edge_color = 'red')
# plt.savefig("ba.png")           #输出方式1: 将图像存为一个png格式的图片文件
# plt.show()                            #输出方式2: 在窗口中显示这幅图像

#-------------------
# Snow Ball Sampler
#-------------------

sampler = SnowBallSampler()
sampler.__init__(number_of_nodes=1000, k=100, seed=42)
new_graph = sampler.sample(graph)


#画图
pos = nx.spring_layout(new_graph)
#nx.draw_spring(graph, node_size=15, node_color=node_lable, cmap=plt.get_cmap('hsv'), with_labels = True )
plt.figure(2)
nx.draw(new_graph, node_size=20, cmap=plt.get_cmap('hsv'), with_labels = True, font_size = 6, edge_color = 'red')
plt.savefig("ba2.png")           #输出方式1: 将图像存为一个png格式的图片文件
plt.show()                            #输出方式2: 在窗口中显示这幅图像
#----------------------------
# Depth First Search Sampler
#----------------------------

sampler = DepthFirstSearchSampler(number_of_nodes=graph.number_of_nodes())

new_graph = sampler.sample(graph)

#------------------------------
# Breadth First Search Sampler
#------------------------------

sampler = BreadthFirstSearchSampler(number_of_nodes=graph.number_of_nodes())

new_graph = sampler.sample(graph)

#---------------------------------
# Loop Erased Random Walk Sampler
#---------------------------------

sampler = LoopErasedRandomWalkSampler()

new_graph = sampler.sample(graph)

#-------------------------------------------
# Common Neighbor Aware Random Walk Sampler
#-------------------------------------------

sampler = NonBackTrackingRandomWalkSampler()

new_graph = sampler.sample(graph)

#-------------------------------------------
# Common Neighbor Aware Random Walk Sampler
#-------------------------------------------

sampler = CommonNeighborAwareRandomWalkSampler()

new_graph = sampler.sample(graph)

#--------------------------------------------
# Random Edge Sampler With Partial Induction
#--------------------------------------------

sampler = RandomEdgeSamplerWithPartialInduction()

new_graph = sampler.sample(graph)

#------------------------
# Shortest Path Sampler
#------------------------

sampler = ShortestPathSampler()

new_graph = sampler.sample(graph)

#-------------------------------------------
# Circulated Neighbors Random Walk Sampler
#-------------------------------------------

sampler = CirculatedNeighborsRandomWalkSampler()

new_graph = sampler.sample(graph)

#-----------------------------------------------
# Community Structure Expansion Sampler Example
#-----------------------------------------------

sampler = CommunityStructureExpansionSampler()

new_graph = sampler.sample(graph)



#--------------------------
# Frontier Sampler Example
#--------------------------

sampler = FrontierSampler()

new_graph = sampler.sample(graph)

#---------------------------
# ForestFire Sampler Example
#---------------------------

sampler = ForestFireSampler()

new_graph = sampler.sample(graph)

#-----------------------------
# Random Walk Sampler Example
#-----------------------------

sampler = RandomWalkSampler()

new_graph = sampler.sample(graph)

#-----------------------------
# Random Node Sampler Example
#-----------------------------

sampler = RandomNodeSampler()

new_graph = sampler.sample(graph)

#-----------------------------
# Random Edge Sampler Example
#-----------------------------

sampler = RandomEdgeSampler()

new_graph = sampler.sample(graph)

#--------------------------------------------
# Random Edge Sampler With Induction Example
#--------------------------------------------

sampler = RandomEdgeSamplerWithInduction()

new_graph = sampler.sample(graph)

#------------------------------
# Degree Based Sampler Example
#------------------------------

sampler = DegreeBasedSampler()

new_graph = sampler.sample(graph)

#--------------------------------
# PageRank Based Sampler Example
#--------------------------------

sampler = PageRankBasedSampler()

new_graph = sampler.sample(graph)

#----------------------------------
# Random Node Edge Sampler Example
#----------------------------------

sampler = RandomNodeEdgeSampler()

new_graph = sampler.sample(graph)

#----------------------------------
# Hybrid Node Edge Sampler Example
#----------------------------------

sampler = HybridNodeEdgeSampler()

new_graph = sampler.sample(graph)

#--------------------------------------
# Random Node Neighbor Sampler Example
#--------------------------------------

sampler = RandomNodeNeighborSampler()

new_graph = sampler.sample(graph)

#------------------------------------------
# Random Walk With Restart Sampler Example
#------------------------------------------

sampler = RandomWalkWithRestartSampler()

new_graph = sampler.sample(graph)

#-------------------------------
# Random Walk With Jump Example
#-------------------------------

sampler = RandomWalkWithJumpSampler()

new_graph = sampler.sample(graph)

#-----------------------------------------
# Metropolis Hastings Random Walk Example
#-----------------------------------------

sampler = MetropolisHastingsRandomWalkSampler()

new_graph = sampler.sample(graph)

