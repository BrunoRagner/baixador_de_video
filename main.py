from pytube import YouTube


yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
yt.title()
yt.thumbnail_url()
stream = yt.streams.get_by_itag(22)
stream.download()