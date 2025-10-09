Name:		piper-voice-fa_IR-amir
Version:	2023.09.23
Release:	1
Summary:	Farsi male voice for the Piper TTS system
URL:		https://huggingface.co/rhasspy/piper-voices/tree/main/fa/fa_IR/amir/medium
License:	MIT
BuildArch:	noarch
Group:		System/Multimedia
Provides:	piper-voice
Provides:	piper-voice-fa
Provides:	piper-voice-fa_IR

%sourcelist
https://huggingface.co/rhasspy/piper-voices/resolve/main/fa/fa_IR/amir/medium/fa_IR-amir-medium.onnx
https://huggingface.co/rhasspy/piper-voices/resolve/main/fa/fa_IR/amir/medium/fa_IR-amir-medium.onnx.json

%description
%{summary}

%install
mkdir -p %{buildroot}%{_datadir}/piper/voices
install -c -m 644 %{S:0} %{S:1} %{buildroot}%{_datadir}/piper/voices/

%files
%{_datadir}/piper/voices/*
