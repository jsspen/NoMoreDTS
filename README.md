# NoMoreDTS

A simple Python script to convert audio tracks in video files using FFMPEG.
To be honest this is very much a "just for me" kind of thing, built for my own needs BUT here it is!

# Why NoMoreDTS?

I have a television that cannot play direct play DTS encoded audio (or FLAC) and my little Raspberry Pi can get really bogged down trying to transcode audio on the fly. I had previously encoded many of my files with DTS audio without realizing the limitations of my (admittedly old) TV. I've got years with of archived video and when I go to watch something and my media player shows "DTS Audio" my whole family groans. There's nothing at all wrong with DTS (or FLAC) and I _wish_ I could play them... but for now I need to convert them.

# Default Settings

Across a variety of testing I have settled on the following FFMPEG command
`-map 0 -c:v copy -c:a ac3 -b:a 640k -c:s copy`
This ensures the video track is copied, not re-encoded, any subtitles are preserved, and the audio is re-encoded as AC3 at 640K quality

# Usage

The code is heavily commented to explain the choices I have made and how to operate it. It's pretty straightforward! As long as you have FFMPEG installed (and available on your path) you should have no trouble using it.
