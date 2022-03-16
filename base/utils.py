import base64
import matplotlib.pyplot as plt
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_chart(x,y):
    plt.switch_backend('AGG')
    # plt.figure(figsize=(3,3))
    plt.plot(x,y)    
    chart = get_graph()
    return chart
