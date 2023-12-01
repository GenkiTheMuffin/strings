# how to utf-8


##  Prvych 127 znakov je rovnako ako ascii len s extra 0 na zaciatku, cize A = 65 co by bolo 01000011 pre cisla viac ako 256 ich len rozseka na viacero bytov

### 110xxxxx 10xxxxxx

## dve jednotky na zaciatku znamena ze cislo bude v dvoch bytoch, 10 na zaciatku znamena ze to je pokracovanie to nam dava celkom 11 volnych miest , potom len tie zaciatky dame prec a mozme vypocitat cislo

## pre try byty by to vizeralo takto:
 ### 1110xxxx 10xxxxxx 10xxxxxx

## toto ide az do
### 1111110x 10xxxxxx 10xxxxxx 10xxxxxx ......  

#### ***fin***
