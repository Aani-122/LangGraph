from langgraph.graph import StateGraph, END, START
from typing import TypedDict
from show import show_graph

class InputState(TypedDict):
    string_value: str
    number_value: int

def modify_state(state: InputState) -> InputState:
    state["string_value"] += "a"
    state["number_value"] += 1
    return state

def router(state: InputState) -> str:
    if state["number_value"] < 5:
        return "branch_1"
    else:
        return "__end__"

graph = StateGraph(InputState)
graph.add_node("branch_1", modify_state)
graph.add_node("branch_2", modify_state)
graph.add_edge(START, "branch_1")
graph.add_edge("branch_1", "branch_2")
graph.add_conditional_edges(
    "branch_2",router,{"branch_1": "branch_1", "__end__": END})

runnable = graph.compile()

print(runnable.invoke({"string_value": "b", "number_value": 0}))
show_graph(runnable)








