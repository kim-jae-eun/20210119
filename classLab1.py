class Member:
    def __init__(self):
        self.name = None
        self.account = None
        self.passwd = None
        self.birthyear = None
a = Member()
b = Member()
c = Member()
# d = Member()
a.name, a.account, a.passwd, a.birthyear = '정포도', 'abc@never.com', 'aabbcc', 2000
b.name, b.account, b.passwd, b.birthyear = '박수박', 'zzz@never.com', 'zzz123', 1999
c.name, c.account, c.passwd, c.birthyear = '김딸기', 'berry@never.com', '0000', 2001
members = [a, b, c]
# members=[a, b, c, d]
for i in members:
    print(f'회원{members.index(i)+1} : {i.name}({i.account}, {i.passwd}, {i.birthyear})')