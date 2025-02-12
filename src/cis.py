import cv2

def mp4write(video, filename, fps):
  size = (video.shape[1], video.shape[0])
  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  out = cv2.VideoWriter(filename, fourcc, fps, size)
  for i in range(video.shape[3]):
    out.write(video[:,:,:,i])

import numpy as np    
import plotly.graph_objects as go    
    
def stem3(z):
  if z.ndim==1:
    Y=1
    X=z.shape[0]
  else:
    X,Y=z.shape

  xl=np.arange(X)
  yl=np.arange(Y)
  x,y=np.meshgrid(xl,yl)

  z= z.flatten()
  stemsx = []
  stemsy = []
  stemsz = []
  for xs, ys in zip(x.flatten(), y.flatten()):
    stemsx.extend([xs, xs, None])
    stemsy.extend([ys, ys, None])

  for zs in z:
    stemsz.extend([0, zs, None])

  fig= go.Figure(go.Scatter3d(x=stemsx, y=stemsy, z=stemsz, mode= "lines",
                            line_width=2, line_color="RoyalBlue"))
  fig.add_trace(go.Scatter3d(x=x.flatten(), y=y.flatten(), z=z, mode="markers",
                           marker_size=1,
                           marker_color="Red"))
  fig.update_layout(
                  width=800, height=800,
                  showlegend=False)
  fig.show()    

def mesh(z):
    data = [ go.Surface(z = z) ]
    fig = go.Figure(data = data)
    fig.update_layout(
        width=800, height=800,
        showlegend=False)
    fig.show()
