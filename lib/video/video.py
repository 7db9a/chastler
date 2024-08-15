class Video:
    def __init__(self, file_path: str):
        """
        Initializes the Chastler instance with the provided MP4 file path.
        """
        pass
    
    def load_file(self) -> None:
        """
        Loads the MP4 file for processing.
        """
        pass
    
    def calculate_file_size(self) -> int:
        """
        Calculates and returns the size of the MP4 file in bytes.
        """
        pass
    
    def get_duration(self) -> float:
        """
        Returns the duration of the MP4 file in seconds.
        """
        pass
    
    def get_resolution(self) -> tuple[int, int]:
        """
        Returns the resolution of the MP4 file as a tuple (width, height).
        """
        pass
    
    def get_bitrate(self) -> int:
        """
        Returns the bitrate of the MP4 file in kbps.
        """
        pass
    
    def get_frame_rate(self) -> float:
        """
        Returns the frame rate of the MP4 file.
        """
        pass
    
    def get_audio_channels(self) -> int:
        """
        Returns the number of audio channels in the MP4 file.
        """
        pass

