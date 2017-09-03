import plotly.plotly as py
import plotly.graph_objs as go


x = ['Go']
# y = y_go_async_get = [1.975]
# y = y_go_async_head = [1.93]
# y = y_go_async_get_mem = [90]
y = y_go_async_head_mem = [92]

trace_go = go.Bar(
            x=x,
            y=y,
            name='Go Async',
         )

x = ['Go']
# y = y_go_sync_get = [14.095]
# y = y_go_sync_head = [4.405]
# y = y_go_sync_get_mem = [91]
y = y_go_sync_head_mem = [92]

trace_go1 = go.Bar(
            x=x,
            y=y,
            name='Go Sync',
        )

x = ['urllib3', 'requests', 'aiohttp']
# y = y_python_async_get = [3.985, 14.266, 4.046]
# y = y_python_async_head = [4.087, 13.737, 7.306]
# y = y_python_async_get_mem = [33, 56, 24]
y = y_python_async_head_mem = [56, 43, 25]

trace_py = go.Bar(
            x=x,
            y=y,
            name='Python Async'
        )

x = ['urllib3', 'requests']
# y = y_python_sync_get = [4.034, 15.397]
# y = y_python_sync_head = [4.08, 15.37]
# y = y_python_sync_get_mem = [24, 50]
y = y_python_sync_get_mem = [36, 46]

trace_py1 = go.Bar(
            x=x,
            y=y,
            name='Python Sync'
        )

data = [trace_go, trace_go1, trace_py, trace_py1]
layout = go.Layout(
            barmode='group',
            title='Go/Python Sync/Async HEAD requests time taken',
            yaxis=dict(
                    title='Time (in seconds)'
                )
        )

fig = go.Figure(data=data, layout=layout)
py.iplot(data, filename='async_sync_head_mem')
