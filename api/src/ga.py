import random
import numpy as np

def cross(p1, p2):
    c1 = list()
    c2 = list()

    # 交差が発生する確率
    p_corss = random.randint(0,100)
    # 突然変異が発生する確率
    p_mut = random.randint(0,10)

    # 突然変異のみ
    if p_corss < 20:
        c1 = p1
        c2 = p2

        if p_mut == 0:
            num_mut_element = random.randint(0,3)
            for i in range(num_mut_element):
                selectModel = random.randint(0,2)
                if selectModel == 1:
                    c1 = mutation(c1)
                else:
                    c2 = mutation(c2)
    
    # 交差 + 突然変異
    else:
        sepPos1 = random.randint(0,9)
        sepPos2 = random.randint(0,9)

        if sepPos1 > sepPos2:
            swap = sepPos1
            sepPos1 = sepPos2
            sepPos2 = swap
        
        for i in range(sepPos1):
            c1.append(p1[i])
            c2.append(p2[i])
        for i in range(sepPos1,sepPos2):
            c1.append(p2[i])
            c2.append(p1[i])
        for i in range(sepPos2,9):
            c1.append(p1[i])
            c2.append(p2[i])
        
        if p_mut == 0:
            num_mut_element = random.randint(0,3)
            for i in range(num_mut_element):
                selectModel = random.randint(0,2)
                if selectModel == 1:
                    c1 = mutation(c1)
                else:
                    c2 = mutation(c2)
    
    return c1, c2


def mutation(c):
    element = random.randint(0,9)

    if element == 2 or element == 5 or element == 8:
        value_mut = random.randint(0,100)-50
        if c[element] + value_mut > 180:
            c[element] = c[element] + value_mut - 180
        elif c[element] + value_mut < 0:
            c[element] = c[element] + value_mut + 180
    else:
        else_mut = random.randint(0,200)-10
        if c[element] + else_mut > 255:
            c[element] = c[element] + else_mut - 255
        elif c[element] + else_mut < 0:
            c[element] = c[element] + else_mut + 255
    return c


def roulett_select(models):
    score_sum = 0
    for m in models:
        score_sum = score_sum + m.score

    for m in models:
        m.p = m.score*1.0/score_sum * 100

    temp = random.randint(0,100)
    # この下怪しい
    for m in models:
        temp = temp - m.p
        if temp <= 0:
            return (m)

    return models

# 関数全体を要確認
def elite_select(models):
    score_list = list()
    for m in models:
        score_list.append(m.score)
    
    elite = np.array(score_list)
    b = np.where(elite == elite.max())
    elite_num = random.choice(b[0])

    S = np.array(score_list)
    return elite_num, S.argsort()[2]


