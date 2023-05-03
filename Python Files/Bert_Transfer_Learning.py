import torch.nn as nn
from arabert.preprocess import ArabertPreprocessor
from transformers import AutoTokenizer,AutoModel,AdamW
import numpy as np
import torch


class BERT_Arch(nn.Module):
    def __init__(self, bert):
      super(BERT_Arch, self).__init__()
      self.bert = bert
      self.dropout = nn.Dropout(0.1)            # dropout layer
      self.relu =  nn.ReLU()                    # relu activation function
      self.fc1 = nn.Linear(768,512)             # dense layer 1
      self.fc2 = nn.Linear(512,2)               # dense layer 2 (Output layer)
      self.softmax = nn.LogSoftmax(dim=1)       # softmax activation function
    def forward(self, sent_id, mask):           # define the forward pass
      cls_hs = self.bert(sent_id, attention_mask=mask)['pooler_output']
                                                # pass the inputs to the model
      x = self.fc1(cls_hs)
      x = self.relu(x)
      x = self.dropout(x)
      x = self.fc2(x)                           # output layer
      x = self.softmax(x)                       # apply softmax activation
      return x

def create_model():
    model_name = "aubmindlab/bert-base-arabertv2"
    arabert_prep = ArabertPreprocessor(model_name=model_name)
    arabert_tokenizer = AutoTokenizer.from_pretrained(model_name)
    arabert_model = AutoModel.from_pretrained(model_name)
    model = BERT_Arch(arabert_model)
    model.load_state_dict(torch.load('weights\c3_new_model_weights.pt'))
    return arabert_prep,arabert_tokenizer,model

def softmax(x):
    """Compute softmax values for each set of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

def apply_model(preprocessor,tokenizer,model,text):
    preprocessed = [preprocessor.preprocess(text)]
    tokens=tokenizer.batch_encode_plus(
    preprocessed,
    max_length=24,
    padding="max_length",
    truncation=True
    )
    input_ids = torch.tensor(tokens['input_ids'])
    attention_masks = torch.tensor(tokens['attention_mask'])
    with torch.no_grad():
        preds=model(input_ids,attention_masks)

        preds=preds.detach().cpu().numpy()
    preds_vec=preds[0]
    max_value=max(preds_vec)
    newpreds=[x-max_value for x in preds_vec]
    outputpreds=softmax(newpreds)
    print(outputpreds)
    index=np.argmax(outputpreds)
    percentage=outputpreds[index]
    print(percentage)
    #index=outputpreds
    return index,percentage
