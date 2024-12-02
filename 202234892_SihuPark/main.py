import cv2
from utils import preprocess_frame, region_of_interest, detect_lanes

def main():
    video = cv2.VideoCapture('./Footage/tunnel.mp4')

    if not video.isOpened():
        print("Error: Could not open the video file.")
        return
    
    fps = video.get(cv2.CAP_PROP_FPS)
    delay = int(1000 / fps / 3)

    while True:
        # Read a frame from the video
        ret, frame = video.read()
        if not ret:
            print("End of video or cannot read video.")
            break

        edges = preprocess_frame(frame)
        masked_edges = region_of_interest(edges)
        output_frame = detect_lanes(masked_edges, frame)

        cv2.imshow('Lane Detection Results', output_frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break


    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()