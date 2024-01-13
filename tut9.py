chess =["knight","bishop","king","queen","pawn","rook","check"]
print(chess[0],chess[-1])
#print(len(chess))
#print(chess[0::2])
chess.sort()#changes the list itself
print(chess)
chess.reverse()#changes the list itself
chess.append("GM")#adds at last
chess.insert(1,"e4")
chess.remove("e4")
chess.pop()
#print(chess.count("king"))
print(chess)
chess[-1]="diagonal"
print(chess)

