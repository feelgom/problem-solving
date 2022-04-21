# https://programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    cand = []
    m = m.replace("C#", 'c')
    m = m.replace("D#", 'd')
    m = m.replace("F#", 'f')
    m = m.replace("G#", 'g')
    m = m.replace("A#", 'a')

    for i in range(len(musicinfos)):
        info = musicinfos[i]
        start_str, end_str, name, song = info.split(',')
        song = song.replace("C#", 'c')
        song = song.replace("D#", 'd')
        song = song.replace("F#", 'f')
        song = song.replace("G#", 'g')
        song = song.replace("A#", 'a')
        start = int(start_str[0:2])*60 + int(start_str[3:5])
        end = int(end_str[0:2])*60 + int(end_str[3:5])
        length = end - start
        
        iter_number = length // len(song) +1
        song = (song*iter_number)[:length]
        
        if m in song:
            cand.append([length-i/10, name])
    
    if len(cand) == 0:
        return "(None)"
    
    cand.sort(reverse=True)
    return cand[0][1]

if __name__=="__main__":
    m = ["ABCDEFG", "CC#BCC#BCC#BCC#B", "ABC"]
    musicinfos = [["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"], ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"], ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]]
    answer = ["HELLO", "FOO", "WORLD"]
    for i in range(len(m)):
        print( solution(m[i], musicinfos[i]) == answer[i],  solution(m[i], musicinfos[i]))