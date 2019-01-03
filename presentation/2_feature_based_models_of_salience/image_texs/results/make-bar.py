import matplotlib.pyplot as plt
from matplotlib import colors
plt.style.use('ggplot')
ap_color = colors.cnames["coral"]
apsal_color = colors.cnames["green"]
cos_color = colors.cnames["cornflowerblue"]
ls_color = colors.cnames["red"]
fsls_color = colors.cnames["tomato"]
lscos_color = colors.cnames["purple"]
fslscos_color = colors.cnames["violet"]
alpha=1

ap = [.083, .09, .078]
apsal = [.119, .09, .094]
cos = [.075, .176, .099]
ls = [.097, .207, .112]
lscos = [.115, .189, .127]

plt.suptitle("Stream Summarization Results", fontsize=22)
plt.xlim((.75, 3.75))
plt.xticks([1.25, 2.25, 3.25], ["Expected Gain", "Comp.", "F1"], fontsize=16)

plt.ylim((0, .35))

plt.bar([1], ap[0], width=.1, alpha=alpha, color=ap_color, label="AP")
plt.bar([2], ap[1], width=.1, alpha=alpha, color=ap_color)
plt.bar([3], ap[2], width=.1, alpha=alpha, color=ap_color)

plt.legend()
plt.savefig("uresults1.pdf")

plt.bar([1.1], apsal[0], width=.1, color=apsal_color, alpha=alpha, label="SAP")
plt.bar([2.1], apsal[1], width=.1, color=apsal_color, alpha=alpha)
plt.bar([3.1], apsal[2], width=.1, color=apsal_color, alpha=alpha)

plt.legend()
plt.savefig("uresults2.pdf")

plt.bar([1.2], cos[0], width=.1, color=cos_color, alpha=alpha, label="Cos")
plt.bar([2.2], cos[1], width=.1, color=cos_color, alpha=alpha)
plt.bar([3.2], cos[2], width=.1, color=cos_color, alpha=alpha)

plt.legend()
plt.savefig("uresults3.pdf")

plt.bar([1.3], ls[0], width=.1, color=ls_color, alpha=alpha, label="L2S")
plt.bar([2.3], ls[1], width=.1, color=ls_color, alpha=alpha)
plt.bar([3.3], ls[2], width=.1, color=ls_color, alpha=alpha)

plt.legend()
plt.savefig("uresults4.pdf")

plt.bar([1.4], lscos[0], width=.1, color=lscos_color, alpha=alpha, label="L2SCos")
plt.bar([2.4], lscos[1], width=.1, color=lscos_color, alpha=alpha)
plt.bar([3.4], lscos[2], width=.1, color=lscos_color, alpha=alpha)

plt.legend()
plt.savefig("uresults5.pdf")

plt.close("all")
exit()

ap = [.079, .095, .077]
apsal = [.105, .088, .088]
cos = [.095, .236, .128]
ls = [.136, .306, .162]
lscos = [.162, .276, .184]

plt.suptitle("Latency-Penalized Results", fontsize=22)
plt.xlim((alpha, 3.75))
plt.xticks([1.25, 2.25, 3.25], ["exp. gain", "recall", "F1"], fontsize=16)

plt.ylim((0, .35))

plt.bar([1], ap[0], width=.1, alpha=alpha, color=ap_color, label="AP")
plt.bar([2], ap[1], width=.1, alpha=alpha, color=ap_color)
plt.bar([3], ap[2], width=.1, alpha=alpha, color=ap_color)

plt.legend()
plt.savefig("results1.pdf")

plt.bar([1.1], apsal[0], width=.1, color=apsal_color, alpha=alpha, label="APSal")
plt.bar([2.1], apsal[1], width=.1, color=apsal_color, alpha=alpha)
plt.bar([3.1], apsal[2], width=.1, color=apsal_color, alpha=alpha)

plt.legend()
plt.savefig("results2.pdf")

plt.bar([1.2], cos[0], width=.1, color=cos_color, alpha=alpha, label="Cos")
plt.bar([2.2], cos[1], width=.1, color=cos_color, alpha=alpha)
plt.bar([3.2], cos[2], width=.1, color=cos_color, alpha=alpha)

plt.legend()
plt.savefig("results3.pdf")

plt.bar([1.3], ls[0], width=.1, color=ls_color, alpha=alpha, label="LS")
plt.bar([2.3], ls[1], width=.1, color=ls_color, alpha=alpha)
plt.bar([3.3], ls[2], width=.1, color=ls_color, alpha=alpha)

plt.legend()
plt.savefig("results4.pdf")

plt.bar([1.4], lscos[0], width=.1, color=lscos_color, alpha=alpha, label="LSCos")
plt.bar([2.4], lscos[1], width=.1, color=lscos_color, alpha=alpha)
plt.bar([3.4], lscos[2], width=.1, color=lscos_color, alpha=alpha)

plt.legend()
plt.savefig("results5.pdf")


plt.close("all")




cos = [.095, .236, .128]
fsls = [.164, .22, .157]
fslscos = [.207, .18, .163]

ls = [.136, .306, .162]
lscos = [.162, .276, .184]


plt.suptitle("Latency-Penalized Results", fontsize=22)
plt.xlim((alpha, 3.75))
plt.xticks([1.25, 2.25, 3.25], ["exp. gain", "recall", "F1"], fontsize=16)

plt.ylim((0, .35))

#plt.bar([1], ap[0], width=.1, alpha=alpha, color=ap_color, label="AP")
#plt.bar([2], ap[1], width=.1, alpha=alpha, color=ap_color)
#plt.bar([3], ap[2], width=.1, alpha=alpha, color=ap_color)

#plt.legend()
#plt.savefig("results1.pdf")

#plt.bar([1.1], apsal[0], width=.1, color=apsal_color, alpha=alpha, label="APSal")
#plt.bar([2.1], apsal[1], width=.1, color=apsal_color, alpha=alpha)
#plt.bar([3.1], apsal[2], width=.1, color=apsal_color, alpha=alpha)

#plt.legend()
#plt.savefig("results2.pdf")

plt.bar([1.], cos[0], width=.1, color=cos_color, alpha=alpha, label="Cos")
plt.bar([2.], cos[1], width=.1, color=cos_color, alpha=alpha)
plt.bar([3.], cos[2], width=.1, color=cos_color, alpha=alpha)

plt.bar([1.2], fsls[0], width=.1, color=fsls_color, alpha=alpha, label="LsFS")
plt.bar([2.2], fsls[1], width=.1, color=fsls_color, alpha=alpha)
plt.bar([3.2], fsls[2], width=.1, color=fsls_color, alpha=alpha)

plt.bar([1.3], fslscos[0], width=.1, color=fslscos_color, alpha=alpha, label="LsCosFS")
plt.bar([2.3], fslscos[1], width=.1, color=fslscos_color, alpha=alpha)
plt.bar([3.3], fslscos[2], width=.1, color=fslscos_color, alpha=alpha)



plt.legend()
plt.savefig("fsresults1.pdf")

plt.bar([1.5], ls[0], width=.1, color=ls_color, alpha=alpha, label="LS")
plt.bar([2.5], ls[1], width=.1, color=ls_color, alpha=alpha)
plt.bar([3.5], ls[2], width=.1, color=ls_color, alpha=alpha)


plt.bar([1.6], lscos[0], width=.1, color=lscos_color, alpha=alpha, label="LSCos")
plt.bar([2.6], lscos[1], width=.1, color=lscos_color, alpha=alpha)
plt.bar([3.6], lscos[2], width=.1, color=lscos_color, alpha=alpha)

plt.legend()
plt.savefig("fsresults2.pdf")















