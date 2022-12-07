import os, torch, requests

model_url = 'https://models.silero.ai/models/tts/ru/v3_1_ru.pt'
gpu_available = torch.cuda.is_available()

def speak(text='Тест.', device='cpu', sample_rate=48000, voice='baya'):
    if not os.path.exists('silero.pt'):
        raise FileNotFoundError('silero.pt')
    if device == 'cpu':
        device = torch.device('cpu')
        torch.set_num_threads(4)
    elif device == 'gpu':
        device = torch.device('cuda')
    else:
        raise ValueError('Incorrect device')
    model = torch.package.PackageImporter('silero.pt').load_pickle("tts_models", "model")
    if not voice in model.speakers:
        raise ValueError('Incorrect voice')
    model.to(device)
    return model.apply_tts(text=text,
                             speaker=voice,
                             sample_rate=sample_rate)

def download_model():
    with open('silero.pt', 'wb') as file:
        s = requests.get(model_url, stream=True)
        s.raise_for_status()
        downloaded = 0
        size = int(s.headers.get('Content-Length')) // 512
        for chunk in s.iter_content(chunk_size=512):
            file.write(chunk)
            downloaded += 1
            yield round(downloaded / size * 100)
