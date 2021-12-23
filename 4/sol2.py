input_file=open("input")
*draws,=map(int,input_file.readline().split(","))
input_file.readline()
bingo_boards=[]
board=[]
for l in input_file.readlines():
    if len(l)>1:
        board+=list(map(int,l.split()))
    else:
        bingo_boards.append(board)
        board=[]
bingo_boards.append(board)
masks=[0 for i in range(len(bingo_boards))]
completed=[0 for i in range(len(bingo_boards))]
col=0b1000010000100001000010000
rows_and_cols=[0b11111<<20,0b11111<<15,0b11111<<10,0b11111<<5,0b11111,col,col>>1,col>>2,col>>3,col>>4]

for num in draws:
    next_boards=bingo_boards.copy()
    next_masks=masks.copy()
    for i,board in enumerate(bingo_boards):
        if num in board:
            masks[i]|=1<<board.index(num)
        for bitmask in rows_and_cols:
            if masks[i]&bitmask==bitmask and completed[i]==0:
                completed[i]=1
                break
        if all(completed):
            s=0
            for j,x in enumerate(board):
                s+=(1^((masks[i]>>j)&1))*x
            print(num*s)
            exit()