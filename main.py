from pytube import YouTube

yt = yt
yt = YouTube('')
yt.title()
yt.thumbnail_url()
stream = yt.streams.get_by_itag(22)
stream.download()
