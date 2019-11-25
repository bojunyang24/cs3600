# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    current = problem.getStartState()
    # if already at goal state
    # keep track of steps taken to get to current state
    # tracker = (currentState, listOfActionsTaken)
    tracker = (current, [])
    # initialize stack and closed set, push start state
    open = util.Stack()
    open.push(tracker)
    closed = set()

    while not open.isEmpty():
        tracker = open.pop()
        if problem.isGoalState(tracker[0]):
            return tracker[1]
        if tracker[0] not in closed:
            closed.add(tracker[0])
            for succ in problem.getSuccessors(tracker[0]):
                open.push((succ[0], tracker[1] + [succ[1]]))

    return tracker[1]
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    current = problem.getStartState()
    tracker = (current,[])
    open = util.Queue()
    open.push(tracker)
    """ closed set. Sets can't add lists because they can be changed, which means
    lists are unhashable. But you can add tuples. but you CAN'T add tuples with
    lists inside of them because those lists can be changed. fixed in q5 by using
    a tuple to represent the 4 corners instead of a list
    """
    closed = set()
    while not open.isEmpty():
        tracker = open.pop()
        if problem.isGoalState(tracker[0]):
            return tracker[1]
        if tracker[0] not in closed:
            closed.add(tracker[0])
            for succ in problem.getSuccessors(tracker[0]):
                open.push([succ[0], tracker[1] + [succ[1]]])
    return tracker[1]
    # # util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    currentState = problem.getStartState()
    open = util.PriorityQueue()
    ### tracker = (state, actions, stepcost)
    tracker = (currentState, [], 0)
    open.push((tracker[0], tracker[1], tracker[2]), tracker[2])
    closed = set()

    while not open.isEmpty():
        tracker = open.pop()
        if problem.isGoalState(tracker[0]):
            return tracker[1]
        if tracker[0] not in closed:
            closed.add(tracker[0])
            for succ in problem.getSuccessors(tracker[0]):
                open.push((succ[0], tracker[1] + [succ[1]], tracker[2]
                    + succ[2]), tracker[2] + succ[2])
    return tracker[1]

    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    currentState = problem.getStartState()
    # print currentState
    ## create priorityqueue with lambda function
    open = util.PriorityQueueWithFunction(lambda tracker : heuristic(tracker[0],
        problem) + tracker[2])
    ### tracker = (state, actions, stepcost)
    tracker = (currentState, [], 0)
    open.push(tracker)
    closed = set()

    while not open.isEmpty():
        tracker = open.pop()
        if problem.isGoalState(tracker[0]):
            return tracker[1]
        if tracker[0] not in closed:
            closed.add(tracker[0])
            for succ in problem.getSuccessors(tracker[0]):
                open.push((succ[0], tracker[1] + [succ[1]], tracker[2] + succ[2]))
    return tracker[1]

    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
