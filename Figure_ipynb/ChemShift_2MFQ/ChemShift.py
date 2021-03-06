import numpy as np

# function to load the sparta+ pred file
def LoadPred(file_name,rangestart=27):
    f = open(file_name)
    r = f.readlines()
    content = []
    for i in range(rangestart,len(r)):
        content.append(r[i].split())
    return content

    # The number 28 here depends on the chain number of the protein predicted


def LoadPred_CA(file_name,rangestart=27):
    content = LoadPred(file_name,rangestart)

    CA_list = []
    for i in range(len(content)):
        if content[i][2] == 'CA':
            CA_list.append(content[i])
    
    CA_2shift = [float(item[4]) for item in CA_list]

    return CA_2shift


def LoadPred_CA_2(file_name,rangestart=27):
    content = LoadPred(file_name,rangestart)

    CA_list = []
    for i in range(len(content)):
        if content[i][2] == 'CA':
            CA_list.append(content[i])
    
    CA_2shift = [float(item[3]) for item in CA_list]

    return CA_2shift


def LoadPred_CA_RC(file_name,rangestart=27):
    content = LoadPred(file_name,rangestart)

    CA_list = []
    for i in range(len(content)):
        if content[i][2] == 'CA':
            CA_list.append(content[i])
    
    CA_2shift = [float(item[5]) for item in CA_list]

    return CA_2shift


def LoadPred_Res(file_name,rangestart=27):
    content = LoadPred(file_name,rangestart)

    CA_list = []
    for i in range(len(content)):
        if content[i][2] == 'CA':
            CA_list.append(content[i])
    
    CA_2shift = [item[0]+item[1] for item in CA_list]

    return CA_2shift


def LoadPred_HA(file_name,rangestart=27):
    content = LoadPred(file_name,rangestart)

    HA_list = []
    for i in range(len(content)):
        if content[i][2] == 'HA':
            HA_list.append(content[i])
        elif content[i][2] == 'HA2':
            HA_list.append(content[i])
    
    HA_2shift = [float(item[4]) for item in HA_list]

    return HA_2shift


def LoadPred_HN(file_name,rangestart=27):
    content = LoadPred(file_name,rangestart)

    HN_list = []
    for i in range(len(content)):
        if content[i][2] == 'HN':
            HN_list.append(content[i])
        elif content[i][2] == 'HA' and content[i][1] == 'P':
            HN_list.append([None,None,None,None,201])
    
    HN_2shift = [None] + [float(item[4]) for item in HN_list]
    HN_2shift_new = [None if i == 201 else i for i in HN_2shift]

    return HN_2shift_new


def LoadPred_N(file_name,rangestart=27):
    content = LoadPred(file_name,rangestart)

    N_list = []
    for i in range(len(content)):
        if content[i][2] == 'N':
            N_list.append(content[i])
        elif content[i][2] == 'HA' and content[i][1] == 'P':
            N_list.append([None,None,None,None,201])
    
    N_2shift = [None] + [float(item[4]) for item in N_list]
    N_2shift_new = [None if i == 201 else i for i in N_2shift]

    return N_2shift_new


def LoadPred_C(file_name,rangestart=27):
    content = LoadPred(file_name,rangestart)

    C_list = []
    for i in range(len(content)):
        if content[i][2] == 'C':
            C_list.append(content[i])
    
    C_2shift = [float(item[4]) for item in C_list] + [None]

    return C_2shift


def LoadPred_CB(file_name,rangestart=27):
    content = LoadPred(file_name,rangestart)

    CB_list = []
    for i in range(len(content)):
        if content[i][2] == 'CB':
            CB_list.append(content[i])
        elif content[i][2] == 'CA' and content[i][1] == 'G':
            CB_list.append([None,None,None,None,201])
    
    CB_2shift = [float(item[4]) for item in CB_list]
    CB_2shift_new = [None if i == 201 else i for i in CB_2shift]

    return CB_2shift_new



def RMSD(list_1,list_2):
    if len(list_1) != len(list_2):
        return 0
    else:
        rmsd = 0
        count = 0
        for i in range(len(list_1)-1):                      # here minus 1 to delete the final residue, for sparta+ only predicts it into 0
            if list_1[i] != None and list_2[i] != None:
                rmsd += (list_1[i]-list_2[i])**2
                count += 1
            else:
                pass
        return np.sqrt(rmsd/count)





def AvgChemShift_CA_2(File_1,File_2,File_3,File_4,File_5,rangestart=27):
    CA_ShiftSim1 = LoadPred_CA_2(File_1,rangestart)
    CA_ShiftSim2 = LoadPred_CA_2(File_2,rangestart)
    CA_ShiftSim3 = LoadPred_CA_2(File_3,rangestart)
    CA_ShiftSim4 = LoadPred_CA_2(File_4,rangestart)
    CA_ShiftSim5 = LoadPred_CA_2(File_5,rangestart)

    CA_ShiftAvg = [(CA_ShiftSim1[i]+CA_ShiftSim2[i]+CA_ShiftSim3[i]+CA_ShiftSim4[i]+CA_ShiftSim5[i])/5 for i in range(len(CA_ShiftSim1))]
    return CA_ShiftAvg



def AvgChemShift_CA(File_1,File_2,File_3,File_4,File_5,rangestart=27):
    CA_ShiftSim1 = LoadPred_CA(File_1,rangestart)
    CA_ShiftSim2 = LoadPred_CA(File_2,rangestart)
    CA_ShiftSim3 = LoadPred_CA(File_3,rangestart)
    CA_ShiftSim4 = LoadPred_CA(File_4,rangestart)
    CA_ShiftSim5 = LoadPred_CA(File_5,rangestart)

    CA_ShiftAvg = [(CA_ShiftSim1[i]+CA_ShiftSim2[i]+CA_ShiftSim3[i]+CA_ShiftSim4[i]+CA_ShiftSim5[i])/5 for i in range(len(CA_ShiftSim1))]
    return CA_ShiftAvg



def AvgChemShift_HA(File_1,File_2,File_3,File_4,File_5,rangestart=27):
    HA_ShiftSim1 = LoadPred_HA(File_1,rangestart)
    HA_ShiftSim2 = LoadPred_HA(File_2,rangestart)
    HA_ShiftSim3 = LoadPred_HA(File_3,rangestart)
    HA_ShiftSim4 = LoadPred_HA(File_4,rangestart)
    HA_ShiftSim5 = LoadPred_HA(File_5,rangestart)

    HA_ShiftAvg = [(HA_ShiftSim1[i]+HA_ShiftSim2[i]+HA_ShiftSim3[i]+HA_ShiftSim4[i]+HA_ShiftSim5[i])/5 for i in range(len(HA_ShiftSim1))]
    return HA_ShiftAvg


def AvgChemShift_HN(File_1,File_2,File_3,File_4,File_5,rangestart=27):
    HN_ShiftSim1 = LoadPred_HN(File_1,rangestart)
    HN_ShiftSim2 = LoadPred_HN(File_2,rangestart)
    HN_ShiftSim3 = LoadPred_HN(File_3,rangestart)
    HN_ShiftSim4 = LoadPred_HN(File_4,rangestart)
    HN_ShiftSim5 = LoadPred_HN(File_5,rangestart)

    HN_ShiftAvg = [(HN_ShiftSim1[i]+HN_ShiftSim2[i]+HN_ShiftSim3[i]+HN_ShiftSim4[i]+HN_ShiftSim5[i])/5 if HN_ShiftSim1[i] != None else HN_ShiftSim1[i] for i in range(len(HN_ShiftSim1))]
    return HN_ShiftAvg


def AvgChemShift_N(File_1,File_2,File_3,File_4,File_5,rangestart=27):
    N_ShiftSim1 = LoadPred_N(File_1,rangestart)
    N_ShiftSim2 = LoadPred_N(File_2,rangestart)
    N_ShiftSim3 = LoadPred_N(File_3,rangestart)
    N_ShiftSim4 = LoadPred_N(File_4,rangestart)
    N_ShiftSim5 = LoadPred_N(File_5,rangestart)

    N_ShiftAvg = [(N_ShiftSim1[i]+N_ShiftSim2[i]+N_ShiftSim3[i]+N_ShiftSim4[i]+N_ShiftSim5[i])/5 if N_ShiftSim1[i] != None else N_ShiftSim1[i] for i in range(len(N_ShiftSim1))]
    return N_ShiftAvg


def AvgChemShift_C(File_1,File_2,File_3,File_4,File_5,rangestart=27):
    C_ShiftSim1 = LoadPred_C(File_1,rangestart)
    C_ShiftSim2 = LoadPred_C(File_2,rangestart)
    C_ShiftSim3 = LoadPred_C(File_3,rangestart)
    C_ShiftSim4 = LoadPred_C(File_4,rangestart)
    C_ShiftSim5 = LoadPred_C(File_5,rangestart)

    C_ShiftAvg = [(C_ShiftSim1[i]+C_ShiftSim2[i]+C_ShiftSim3[i]+C_ShiftSim4[i]+C_ShiftSim5[i])/5 if C_ShiftSim1[i] != None else C_ShiftSim1[i] for i in range(len(C_ShiftSim1))]
    return C_ShiftAvg


def AvgChemShift_CB(File_1,File_2,File_3,File_4,File_5,rangestart=27):
    CB_ShiftSim1 = LoadPred_CB(File_1,rangestart)
    CB_ShiftSim2 = LoadPred_CB(File_2,rangestart)
    CB_ShiftSim3 = LoadPred_CB(File_3,rangestart)
    CB_ShiftSim4 = LoadPred_CB(File_4,rangestart)
    CB_ShiftSim5 = LoadPred_CB(File_5,rangestart)

    CB_ShiftAvg = [(CB_ShiftSim1[i]+CB_ShiftSim2[i]+CB_ShiftSim3[i]+CB_ShiftSim4[i]+CB_ShiftSim5[i])/5 if CB_ShiftSim1[i] != None else CB_ShiftSim1[i] for i in range(len(CB_ShiftSim1))]
    return CB_ShiftAvg


