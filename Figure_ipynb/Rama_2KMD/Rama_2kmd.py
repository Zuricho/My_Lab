import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from scipy import interpolate


ramaEW = np.loadtxt("phipsi_2kmd_1_EW.dat",skiprows=1)
ramaEWCMAP = np.loadtxt("phipsi_2kmd_1_EW_CMAP.dat",skiprows=1)
ramaD = np.loadtxt("phipsi_2kmd_1_D.dat",skiprows=1)
ramaDCMAP = np.loadtxt("phipsi_2kmd_1_D_CMAP.dat",skiprows=1)

ramaEW_2 = np.loadtxt("phipsi_2kmd_2_EW.dat",skiprows=1)
ramaEWCMAP_2 = np.loadtxt("phipsi_2kmd_2_EW_CMAP.dat",skiprows=1)
ramaD_2 = np.loadtxt("phipsi_2kmd_2_D.dat",skiprows=1)
ramaDCMAP_2 = np.loadtxt("phipsi_2kmd_2_D_CMAP.dat",skiprows=1)


plt.subplots(figsize=(6,6))


plt.subplot(221)

cov = np.vstack([ramaEW[:,1],ramaEW[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaEW[:,1],ramaEW[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)
plt.xticks([])


plt.subplot(222)

cov = np.vstack([ramaEWCMAP[:,1],ramaEWCMAP[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaEWCMAP[:,1],ramaEWCMAP[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)
plt.xticks([])
plt.yticks([])


plt.subplot(223)

cov = np.vstack([ramaD[:,1],ramaD[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaD[:,1],ramaD[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)


plt.subplot(224)

cov = np.vstack([ramaDCMAP[:,1],ramaDCMAP[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaDCMAP[:,1],ramaDCMAP[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)
plt.yticks([])


plt.tight_layout(pad=0.01)

plt.savefig('Rama_2kmd.png',dpi=200)
plt.show()

# TALOS-N data
data = np.array([0.041,0.004,0.000,0.002,0.000,0.002,0.000,0.000,0.000,0.002,0.000,0.000,0.004,0.021,0.060,0.136,0.160,0.105,0.072,0.014,0.001,0.001,0.000,0.000,0.000,0.000,0.001,0.000,0.000,0.001,0.006,0.056,0.182,0.320,0.384,0.246,0.102,0.014,0.001,0.000,0.000,0.000,0.000,0.010,0.000,0.000,0.000,0.000,0.035,0.113,0.290,0.493,0.521,0.322,0.069,0.007,0.001,0.000,0.000,0.000,0.002,0.000,0.000,0.000,0.000,0.000,0.021,0.097,0.234,0.422,0.427,0.239,0.020,0.003,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.044,0.135,0.208,0.180,0.096,0.008,0.000,0.000,0.000,0.001,0.000,0.004,0.000,0.000,0.000,0.000,0.000,0.000,0.006,0.047,0.082,0.063,0.034,0.003,0.000,0.002,0.000,0.003,0.001,0.009,0.029,0.008,0.000,0.000,0.000,0.000,0.005,0.014,0.007,0.022,0.003,0.000,0.001,0.000,0.001,0.001,0.011,0.000,0.009,0.008,0.004,0.001,0.001,0.001,0.003,0.000,0.000,0.000,0.003,0.000,0.000,0.001,0.001,0.003,0.009,0.001,0.006,0.005,0.000,0.001,0.000,0.001,0.000,0.000,0.001,0.001,0.000,0.000,0.000,0.000,0.002,0.000,0.000,0.002,0.001,0.001,0.001,0.000,0.000,0.001,0.001,0.001,0.001,0.001,0.000,0.000,0.003,0.000,0.002,0.002,0.000,0.000,0.002,0.000,0.001,0.000,0.006,0.005,0.002,0.002,0.000,0.002,0.000,0.002,0.004,0.003,0.001,0.003,0.000,0.000,0.003,0.000,0.007,0.003,0.007,0.004,0.002,0.001,0.002,0.001,0.000,0.001,0.000,0.004,0.003,0.002,0.000,0.002,0.002,0.003,0.009,0.007,0.000,0.000,0.000,0.000,0.001,0.000,0.001,0.000,0.004,0.002,0.004,0.002,0.001,0.000,0.001,0.000,0.000,0.004,0.003,0.002,0.000,0.000,0.000,0.000,0.002,0.001,0.000,0.001,0.001,0.000,0.000,0.000,0.005,0.000,0.000,0.000,0.002,0.002,0.000,0.001,0.002,0.000,0.000,0.004,0.000,0.001,0.000,0.001,0.000,0.000,0.000,0.002,0.000,0.000,0.000,0.000,0.000,0.001,0.000,0.003,0.000,0.001,0.005,0.002,0.000,0.001,0.000,0.001,0.000,0.002,0.000,0.000,0.000,0.001,0.000,0.003,0.004,0.009,0.005,0.011,0.004,0.002,0.000,0.000,0.000,0.000,0.000,0.001,0.000,0.000,0.002,0.001,0.004,0.010,0.031,0.036,0.028])
data = data.reshape((18,18)).T
data = np.flip(data,0)


cubic = interpolate.interp2d(np.arange(0,360,20),np.arange(0,360,20),data, kind='cubic')
x_new = np.arange(0,360,0.1)
y_new = np.arange(0,360,0.1)
cubic_plot = cubic(x_new, y_new)

plt.subplots(figsize=(15,3))


plt.subplot(151)
plt.imshow(cubic_plot,cmap="jet")
plt.xticks([])
plt.yticks([])


plt.subplot(152)

cov = np.vstack([ramaEW[:,1],ramaEW[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaEW[:,1],ramaEW[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)
plt.xticks([])
plt.yticks([])


plt.subplot(153)

cov = np.vstack([ramaEWCMAP[:,1],ramaEWCMAP[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaEWCMAP[:,1],ramaEWCMAP[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)
plt.xticks([])
plt.yticks([])


plt.subplot(154)

cov = np.vstack([ramaD[:,1],ramaD[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaD[:,1],ramaD[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)
plt.xticks([])
plt.yticks([])


plt.subplot(155)

cov = np.vstack([ramaDCMAP[:,1],ramaDCMAP[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaDCMAP[:,1],ramaDCMAP[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)
plt.xticks([])
plt.yticks([])


plt.tight_layout(pad=0.01)

plt.savefig('Rama_2kmd_A.png',dpi=200)



# seconde figure
plt.subplots(figsize=(6,6))


plt.subplot(221)

cov = np.vstack([ramaEW_2[:,1],ramaEW_2[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaEW_2[:,1],ramaEW_2[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)
plt.xticks([])


plt.subplot(222)

cov = np.vstack([ramaEWCMAP_2[:,1],ramaEWCMAP_2[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaEWCMAP_2[:,1],ramaEWCMAP_2[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)
plt.xticks([])
plt.yticks([])


plt.subplot(223)

cov = np.vstack([ramaD_2[:,1],ramaD_2[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaD_2[:,1],ramaD_2[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)


plt.subplot(224)

cov = np.vstack([ramaDCMAP_2[:,1],ramaDCMAP_2[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaDCMAP_2[:,1],ramaDCMAP_2[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)
plt.yticks([])


plt.tight_layout(pad=0.01)

plt.savefig('Rama_2kmd_2.png',dpi=200)
plt.show()

# TALOS-N data
data = np.array([0.013,0.004,0.001,0.001,0.000,0.000,0.002,0.004,0.008,0.008,0.002,0.002,0.000,0.001,0.000,0.010,0.027,0.007,0.015,0.003,0.001,0.001,0.001,0.004,0.013,0.022,0.030,0.029,0.016,0.010,0.004,0.005,0.004,0.024,0.045,0.027,0.023,0.006,0.003,0.001,0.002,0.011,0.030,0.070,0.104,0.086,0.052,0.014,0.005,0.005,0.000,0.016,0.041,0.042,0.016,0.001,0.001,0.003,0.004,0.023,0.067,0.154,0.183,0.162,0.086,0.027,0.002,0.002,0.000,0.004,0.045,0.047,0.040,0.010,0.001,0.000,0.002,0.036,0.149,0.251,0.278,0.178,0.084,0.026,0.011,0.004,0.005,0.041,0.073,0.086,0.044,0.007,0.000,0.000,0.003,0.062,0.218,0.337,0.288,0.152,0.048,0.017,0.008,0.015,0.014,0.065,0.120,0.089,0.013,0.005,0.002,0.001,0.014,0.062,0.196,0.305,0.195,0.073,0.018,0.004,0.002,0.004,0.015,0.046,0.075,0.054,0.002,0.001,0.001,0.002,0.006,0.022,0.100,0.108,0.074,0.018,0.003,0.002,0.000,0.002,0.001,0.018,0.024,0.015,0.000,0.000,0.001,0.000,0.002,0.002,0.014,0.012,0.009,0.002,0.000,0.000,0.000,0.000,0.001,0.006,0.005,0.002,0.000,0.001,0.000,0.001,0.000,0.000,0.002,0.000,0.003,0.000,0.002,0.002,0.001,0.001,0.003,0.001,0.001,0.001,0.001,0.003,0.002,0.001,0.000,0.000,0.000,0.001,0.001,0.003,0.006,0.008,0.003,0.003,0.000,0.000,0.000,0.000,0.003,0.006,0.002,0.002,0.002,0.003,0.003,0.003,0.005,0.011,0.017,0.012,0.005,0.003,0.002,0.001,0.001,0.001,0.004,0.004,0.004,0.001,0.001,0.001,0.002,0.004,0.003,0.016,0.018,0.016,0.001,0.000,0.001,0.001,0.000,0.000,0.000,0.002,0.004,0.003,0.001,0.002,0.001,0.003,0.005,0.007,0.003,0.008,0.003,0.000,0.001,0.000,0.000,0.001,0.000,0.002,0.000,0.001,0.000,0.001,0.000,0.000,0.003,0.004,0.003,0.000,0.000,0.000,0.001,0.000,0.000,0.002,0.003,0.003,0.002,0.002,0.001,0.000,0.001,0.000,0.000,0.000,0.002,0.000,0.000,0.001,0.001,0.001,0.000,0.000,0.001,0.000,0.000,0.000,0.000,0.001,0.002,0.000,0.001,0.000,0.001,0.000,0.000,0.000,0.001,0.002,0.000,0.002,0.004,0.001,0.002,0.001,0.000,0.000,0.001,0.000,0.001,0.003,0.001,0.000,0.001,0.001,0.003,0.000,0.002,0.002])

data = data.reshape((18,18)).T
data = np.flip(data,0)


cubic = interpolate.interp2d(np.arange(0,360,20),np.arange(0,360,20),data, kind='cubic')
x_new = np.arange(0,360,0.1)
y_new = np.arange(0,360,0.1)
cubic_plot = cubic(x_new, y_new)



plt.subplots(figsize=(15,3))


plt.subplot(151)
plt.imshow(cubic_plot,cmap="jet")
plt.xticks([])
plt.yticks([])


plt.subplot(152)

cov = np.vstack([ramaEW_2[:,1],ramaEW_2[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaEW_2[:,1],ramaEW_2[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)
plt.xticks([])
plt.yticks([])


plt.subplot(153)

cov = np.vstack([ramaEWCMAP_2[:,1],ramaEWCMAP_2[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaEWCMAP_2[:,1],ramaEWCMAP_2[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)
plt.xticks([])
plt.yticks([])


plt.subplot(154)

cov = np.vstack([ramaD_2[:,1],ramaD_2[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaD_2[:,1],ramaD_2[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)
plt.xticks([])
plt.yticks([])


plt.subplot(155)

cov = np.vstack([ramaDCMAP_2[:,1],ramaDCMAP_2[:,2]])
density = gaussian_kde(cov)(cov)
plt.scatter(ramaDCMAP_2[:,1],ramaDCMAP_2[:,2],s=2,c=density,cmap='jet')

plt.xlim(-180,180)
plt.ylim(-180,180)
plt.xticks([])
plt.yticks([])


plt.tight_layout(pad=0.01)

plt.savefig('Rama_2kmd_B.png',dpi=200)
plt.show()

