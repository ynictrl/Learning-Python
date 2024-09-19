import random
# random - número entre 0 e 1
# numero_0a100 = random.randrange(0, 11)
# print(numero_0a100)

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# print(random.sample(numeros, k=14))
# random.shuffle(numeros)

    # public void Randomizer()
    # {
    #     string[] cards2 = new string[cards.Length];
    #     int k = 0; 
    #     //string lost = "";
        
    #     for(int i = 0; i < cards.Length; i++)
    #     {
    #         if(i==0)
    #         {
    #             k = Random.Range(0, cards.Length);
    #             lost = k.ToString();
    #         }else{

    #             bool checkIn = true;

    #             while(checkIn)
    #             {
    #                 for(int j=0; j<lost.Length; j++)
    #                 {
    #                     k = Random.Range(0, cards.Length);
    #                     if(lost[j].ToString() == k.ToString())
    #                     {
    #                         checkIn = false;
    #                     }
    #                 }
    #             }
    #             lost += k.ToString();
    #         }

            
    #         cards2[i] = cards[k];
    #     }
    #     cards = cards2;

    # }

def ComPy():
    l1 = [1, 2, 3, 4, 5, 6, 7]
    l2 = []

    for i in range(len(l1)):
        
        if i == 0:
            k = random.randrange(0, len(l1))
            lost = str(k)
        else:
            
            while str(k) in lost:
                k = random.randrange(0, len(l1))
            lost += str(k)
        
        l2.append(l1[k])

    print(f'Lista original:    {l1} \nLista embaralhada: {l2}')

def In(a, b):
    res = False
    for i in range(len(b)):
        if a == b[i]:
            res = True

    return res

def SemPy():
    l1 = [1, 2, 3, 4, 5, 6, 7]
    l2 = []
    lost = ""

    for i in range(len(l1)):

        if i == 0:
            k = random.randrange(0, len(l1))
        else:
            while(In(str(k), lost)):
                k = random.randrange(0, len(l1))
        lost += str(k)
        
        l2.append(l1[k])
    
    return f'Lista original:    {l1} \nLista embaralhada: {l2}'

print(SemPy())
