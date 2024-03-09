# This script defines a long string, counts the number of black characters,
# counts the number of words, finds the longest word and sorts words
# according to the lexicographic order and to the length.

S = """Litwo! Ojczyzno moja! ty jesteś jak zdrowie.
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.
Panno Święta, co Jasnej bronisz Częstochowy
I w Ostrej świecisz Bramie! Ty, co gród zamkowy
Nowogródzki ochraniasz z jego wiernym ludem!
Jak mnie dziecko do zdrowia powróciłaś cudem
(Gdy od płaczącej matki pod Twoję opiekę
Ofiarowany, martwą podniosłem powiekę
I zaraz mogłem pieszo do Twych świątyń progu
Iść za wrócone życie podziękować Bogu),
Tak nas powrócisz cudem na Ojczyzny łono.
Tymczasem przenoś moję duszę utęsknioną
Do tych pagórków leśnych, do tych łąk zielonych,
Szeroko nad błękitnym Niemnem rozciągnionych;
Do tych pól malowanych zbożem rozmaitem,
Wyzłacanych pszenicą, posrebrzanych żytem;
Gdzie bursztynowy świerzop, gryka jak śnieg biała,
Gdzie panieńskim rumieńcem dzięcielina pała,
A wszystko przepasane, jakby wstęgą, miedzą
Zieloną, na niej z rzadka ciche grusze siedzą."""

black_char_sum = sum([1 for char in S if not char.isspace()])  # count as a
# black character if it's not a space

print("Number of black characters:", black_char_sum)

split_S = S.split()  # it's a list, each element is a word

print(split_S)

print("Number of words:", len(split_S))
print("Longest word:", max(split_S, key=len))

split_S.sort(key=str.lower)  # sort in lexicographic order (default way of
# sorting strings), str.lower means that sorting is case-insensitive

print("Words sorted by lexicographic order, case-insensitive:", split_S)

split_S.sort(key=len)  # sort by length

print("Words sorted by length:", split_S)
