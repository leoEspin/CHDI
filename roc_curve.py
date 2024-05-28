def get_roc_curve(actual,probs,thresholds=[0,0.5,1]):
    '''
    Calculates the true and false positive rates for each value in the thresholds
    vector. The input are two arrays containing the actual class values, the predicted
    probabilities and a list with the threshold values between 0 and 1. 
    the function returns two lists, the tprate and fprate respectively
    '''
    tprate=[0]*len(thresholds)
    fprate=tprate.copy()
    confusion=pd.concat([pd.Series(actual,name='Class'),
                 pd.Series(probs,name='PredProb')],axis=1)
    counter=0
    for th in thresholds:
        tpos=len(confusion[(confusion['Class']==1) & (confusion['PredProb']>=th)])
        fneg=len(confusion[(confusion['Class']==1) & (confusion['PredProb']<th)])
        fpos=len(confusion[(confusion['Class']==0) & (confusion['PredProb']>=th)])
        tneg=len(confusion[(confusion['Class']==0) & (confusion['PredProb']<th)])
        tprate[counter]=tpos/(tpos+fneg)
        fprate[counter]=fpos/(fpos+tneg)
        counter+=1
    return tprate,fprate

def get_prec_recall_curve(actual,probs,thresholds=[0,0.5,1]):
  prec=[0]*len(thresholds)
  recall=prec.copy()
  counter=0
  for th in thresholds:
      tpos=len(confusion[(confusion['Class']==1) & (confusion['PredProb']>=th)])
      fneg=len(confusion[(confusion['Class']==1) & (confusion['PredProb']<th)])
      fpos=len(confusion[(confusion['Class']==0) & (confusion['PredProb']>=th)])
      tneg=len(confusion[(confusion['Class']==0) & (confusion['PredProb']<th)])
      prec[counter]=tpos/(tpos+fpos)
      recall[counter]=tpos/(tpos+fneg)
      counter+=1
  return prec, recall
