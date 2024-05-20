import torch
import torch.nn as nn
import warnings
warnings.filterwarnings("ignore")


class RNN_Classiff_max(nn.Module):
    def __init__(
            self, hidden_dim: int, vocab_size: int, num_classes: int, num_layers: int,
            aggregation_type: str = 'max'
    ):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, hidden_dim)
        self.rnn = nn.LSTM(hidden_dim, hidden_dim, num_layers, bidirectional=True, dropout=0.2, batch_first=True)
        self.linear = nn.Linear(hidden_dim * 4, hidden_dim)
        self.batchnorm = nn.BatchNorm1d(hidden_dim)
        self.projection = nn.Linear(hidden_dim, num_classes)
        self.non_lin = nn.Tanh()
        self.dropout = nn.Dropout(p=0.3)

        self.aggregation_type = aggregation_type

    def forward(self, input_batch) -> torch.Tensor:
        embeddings = self.embedding(input_batch)  # [batch_size, seq_len, hidden_dim]
        output, h = self.rnn(embeddings)  # [batch_size, seq_len, hidden_dim]
        output_max = output.max(dim=1)[0]  # [batch_size, hidden_dim] (берем агрегацию по максимуму)
        last_hidden_state = output[:, -1, :]  # эмбеддинг с последнего токена
        output = torch.cat((last_hidden_state, output_max),
                           dim=1)  # конкатенация результата агрегации и эмбеддинга с последнего токена

        concat_output = self.dropout(self.linear(self.non_lin(output)))  # [batch_size, hidden_dim]
        concat_output = self.batchnorm(concat_output)
        prediction = self.projection(self.non_lin(concat_output))  # [batch_size, num_classes]

        return prediction
