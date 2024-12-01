import cv2
from utils import preprocess_frame, region_of_interest, detect_lanes

def main():
    video = cv2.VideoCapture('./Footage/tunnel.mp4')

    if not video.isOpened():
        print("Error: Could not open the video file.")
        return
    

    while True:
        # Read a frame from the video
        ret, frame = video.read()
        if not ret:
            print("End of video or cannot read video.")
            break

        edges = preprocess_frame(frame)
        masked_edges = region_of_interest(edges)
        output_frame = detect_lanes(masked_edges, frame)

        cv2.imshow('Lane Detection', output_frame)

        if cv2.waitKey(8) & 0xFF == ord('q'):
            break


    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()