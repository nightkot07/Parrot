"""import whisper
import torch
import stempeg
from openunmix import predict
from IPython.display import Audio
from .models import MusicHistory
import os


model = whisper.load_model("large-v2")


def decode_music(request, title, file):
    path = ('users/' + str(request.user.id) + '_user/' + 'file.mp3')
    with open(path, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    audio, rate = stempeg.read_stems(
        path,
        sample_rate=44100,
    )
    estimates = predict.separate(
        audio=torch.as_tensor(audio).float(),
        rate=44100,
    )
    new_hist = MusicHistory(title=title, user=request.user, )
    new_hist.save()
    os.mkdir('users/' + str(request.user.id) + '_user/' +
             str(new_hist.id) + '_hist/'
             )
    for target, estimate in estimates.items():
        path = ('users/' + str(request.user.id) + '_user/' +
                str(new_hist.id) + '_hist/' + target + '.mp3'
                )
        audio = Audio(estimate.detach().cpu().numpy()[0], rate=rate, autoplay=True)
        with open(path, 'wb') as f:
            f.write(audio.data)
    path = ('users/' + str(request.user.id) + '_user/' +
            str(new_hist.id) + '_hist/vocals.mp3'
            )
    result = model.transcribe(
        path,
        fp16=False
    )
    path = ('users/' + str(request.user.id) + '_user/' +
            str(new_hist.id) + '_hist/text.txt'
            )
    with open(path, 'wb') as f:
        f.write(result)"""