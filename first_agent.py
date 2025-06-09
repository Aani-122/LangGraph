from langgraph.graph import StateGraph, END, START
from typing import TypedDict
from show import show_graph

class InputState(TypedDict):
    string_value: str
    number_value: int

def modify_state(state: InputState) -> InputState:
    print(f"current state: {state}")
    return state

graph = StateGraph(InputState)
graph.add_node("branch_1", modify_state)
graph.add_node("branch_2", modify_state)
graph.add_edge(START, "branch_1")
graph.add_edge("branch_1", "branch_2")
graph.add_edge("branch_2", END)

runnable = graph.compile()
show_graph(runnable)




