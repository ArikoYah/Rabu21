import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

x = s.slider('pilih rentang', 0.0, 2.0, (.2, .5))
st.write('nilai x:', x)
y = st.slider('set nilai', 0.0,100.0, 25.0)
st.write('nilai y:', y)

t = np.linspace(x[0]*np.pi,x[1]*np.pi,100)
u = np.sin(t)
#st.write('nilai t:','\t)
