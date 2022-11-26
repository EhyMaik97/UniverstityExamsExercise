from models.test import Album
from models.test import Trace
from models.test import Test
import datetime


if __name__ == '__main__':
	# test = Test()
	# test.main()

	trace = Trace(1, "Crazy Of Story", "Cardi B", 2.33)
	trace_2 = Trace(2, "Pure", "Lauren Bacall", 4.44)
	trace_3 = Trace(3, "u2022 TEMPTED", "Bob Marley", 4.23)
	trace_4 = Trace(4, "Let's Play House", "LaVern Baker", 2.11)
	trace_5 = Trace(5, "Many Jungle ", "Kaye Ballard", 5.34)
	trace_6 = Trace(6, "SAD", "XXXTentation", 6.34)
	album = Album(53, [trace, trace_2], "CD", "All Type Music", "By_Tester", str(datetime.date(2022, 11, 26)))

	# Add a trace to Album - method:"add_tracks"
	album.add_tracks([trace_3, trace_4])
	album.add_tracks(trace_5)
	# Check a trace is on the Album - method:"check_existing_trace"
	print("Trace: " + trace_2.title + " is in this album") if album.check_existing_trace(trace_2) else print("Trace: " + trace_2.title + " isn't in this album")
	print("Trace: " + trace_6.title + " is in this album") if album.check_existing_trace(trace_6) else print("Trace: " + trace_6.title + " isn't in this album")
	# Check a trace is on the Album - method:"get_duration_trace"
	print("Trace: " + trace_3.title + ", Duration: " + str(album.get_duration_trace(trace_3)))
	print("Trace: " + trace_4.title + ", Duration: " + str(album.get_duration_trace(trace_4)))
	# Return total duration of the Album - method:"get_total_duration"
	print("Album Total Duration: : " + str(album.get_total_duration()) + " minutes")
	# Cycle tracks in Album by duration in desc
	album_order_tracks = album.cycle_by_duration()
	print("Printing Album tracks by descending durations")
	for trace in reversed(album_order_tracks):
		print("Trace Title: " + trace.title + ", Duration: " + str(trace.duration) + "m")
