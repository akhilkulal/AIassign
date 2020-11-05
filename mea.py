#!/usr/bin/env python

"""
The **General Problem Solver** is a framework for applying *means-ends analysis*
to solve problems that can be specified by a list of initial states, a list of
goal states, and a list of operators that induce state transitions.
Each operator is specified by an action name, a list of precondition states that
must hold before the operator is applied, a list of states that will hold after
the operator is applied (the *add-list*), and a list of states that will no
longer hold after the operator is applied (the *delete-list*).  To achieve a
goal state, GPS uses means-ends analysis: each operator is examined to find one
that contains the goal state in its add-list (it looks for an *appropriate*
operator).  It then tries to achieve all of that operator's precondition states.
If not all of the preconditions can be achieved (the operator is not
*applicable*), then GPS looks for another appropriate operator.  If none exists,
then the goal can't be achieved.  When all of the goal states have been
achieved, the problem is solved.
The following programs demonstrate using GPS to solve some famous AI problems:
- [Monkey and Bananas](examples/gps/monkeys.html)
- [Blocks World](examples/gps/blocks.html)
- [Driving to school](examples/gps/school.html)
This implementation is inspired by chapter 4 of "Paradigms of Artificial
Intelligence Programming" by Peter Norvig.
"""
def mea(ini_s, goal_s, ops):
    pre = 'Executing'
    for op in ops:
        op['add'].append(pre+op['action'])
    f_s = acv_a(ini_s, goal_s, ops, [])
    if len(f_s):
        return [st for st in f_s if st.startswith(pre)]
    else:
        return None
def acv_a(sts, goals, ops, goal_st):
    for go in goals:
        sts = acv(sts, go, ops, goal_st)
        if len(sts) == 0:
            return None
    for goal in goals:
        if goal not in sts:
            return None
    return sts

def acv(sts, goal, ops, goal_st):
    if goal in sts:
        return sts
    if goal in goal_st:
        return None
    for op in ops:
        if goal not in op['add']:
            continue
        res = app_op(op, sts, ops, goal, goal_st)
        if len(res):
            return res
## General Problem Solver
def app_op(op, sts, ops, goal, goal_st):
    res = 
'''
## Achieving subgoals


    
## Using operators

def apply_operator(operator, states, ops, goal, goal_stack):
    """
    Applies operator and returns the resulting states.
    Achieves all of operator's preconditions and returns the states that hold
    after processing its add-list and delete-list.  If any of its preconditions
    cannot be satisfied, returns None.
    """

    debug(len(goal_stack), 'Consider: %s' % operator['action'])

    # Satisfy all of operator's preconditions.
    result = achieve_all(states, ops, operator['preconds'], [goal] + goal_stack)
    if not result:
        return None

    debug(len(goal_stack), 'Action: %s' % operator['action'])

    # Merge the old states with operator's add-list, filtering out delete-list.
    add_list, delete_list = operator['add'], operator['delete']
    return [state for state in result if state not in delete_list] + add_list

'''
## Helper functions

import logging

def debug(level, msg):
    logging.debug(' %s %s' % (level * '  ', msg))
problem = {
    "start": ["at door", "on floor", "has ball", "hungry", "chair at door"],
    "finish": ["not hungry"],
    "ops": [
	{
	    "action": "climb on chair",
	    "preconds": ["chair at middle room", "at middle room", "on floor"],
	    "add": ["at bananas", "on chair"],
	    "delete": ["at middle room", "on floor"]
	},
	{
	    "action": "push chair from door to middle room",
	    "preconds": ["chair at door", "at door"],
	    "add": ["chair at middle room", "at middle room"],
	    "delete": ["chair at door", "at door"]
	},
	{
	    "action": "walk from door to middle room",
	    "preconds": ["at door", "on floor"],
	    "add": ["at middle room"],
	    "delete": ["at door"]
	},
	{
	    "action": "grasp bananas",
	    "preconds": ["at bananas", "empty handed"],
	    "add": ["has bananas"],
	    "delete": ["empty handed"]
	},
	{
	    "action": "drop ball",
	    "preconds": ["has ball"],
	    "add": ["empty handed"],
	    "delete": ["has ball"]
	},
	{
	    "action": "eat bananas",
	    "preconds": ["has bananas"],
	    "add": ["empty handed", "not hungry"],
	    "delete": ["has bananas", "hungry"]
	}
    ]
}

def main():
    start = problem['start']
    finish = problem['finish']
    ops = problem['ops']
    for action in gps(start, finish, ops):
        print action

if __name__ == '__main__':
    main()