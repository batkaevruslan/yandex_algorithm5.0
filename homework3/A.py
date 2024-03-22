def main():
    n = int(input())
    playlists = []
    for _ in range(n):
        k = int(input())
        tracks = input().strip().split()
        playlists.append(tracks)

    result = getSharedPlaylist(playlists)
    print(result[0])
    print(" ".join(result[1]))

def getSharedPlaylist(playlists):
    countByTrack = {}
    for playlist in playlists:
        for track in playlist:
            currentCount = countByTrack.setdefault(track, 0)
            countByTrack[track] = currentCount + 1

    sharedPlaylist = []
    for track, count in countByTrack.items():
        if count == len(playlists):
            sharedPlaylist.append(track)
    sharedPlaylist.sort(key=lambda v: v.upper())
    return (len(sharedPlaylist), sharedPlaylist)
if __name__ == '__main__':
    main()    