from IPython.display import Image, display
from langchain_core.runnables.graph import MermaidDrawMethod

# Generate the graph image
def show_graph(runnable):
    graph_image = runnable.get_graph().draw_mermaid_png(draw_method=MermaidDrawMethod.API)

    # Save the image to a file
    with open('graph_visualization.png', 'wb') as f:
        f.write(graph_image)

    # Display the image
    display(Image(graph_image))







