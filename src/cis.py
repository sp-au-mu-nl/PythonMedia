import cv2

def mp4write(video, filename, fps):
  size = (video.shape[1], video.shape[0])
  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  out = cv2.VideoWriter(filename, fourcc, fps, size)
  for i in range(video.shape[3]):
    out.write(video[:,:,:,i])
