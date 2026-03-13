#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def square(a):
    area_s = a*a
    peri_s = 4*a
    return area_s, peri_s
def rectangle(a,b):
    area_p = a*b
    peri_p = 2*(a+b)
    return area_p, peri_p
def triangle(a,b,c):
    area_t = 0.5 * a * b
    peri_t = a + b + c
    return area_t, peri_t

