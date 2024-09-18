const video = document.getElementById('video');
const startBtn = document.getElementById('startBtn');

navigator.mediaDevices.getUserMedia({ video: true, audio: true })
    .then(stream => {
        video.srcObject = stream;
        const mediaRecorder = new MediaRecorder(stream);
        let chunks = [];

        startBtn.addEventListener('click', () => {
            mediaRecorder.start();
            startBtn.disabled = true;
            setTimeout(() => {
                mediaRecorder.stop();
                startBtn.disabled = false;
            }, 15000); // Stop recording after 15 seconds
        });

        mediaRecorder.ondataavailable = event => {
            chunks.push(event.data);
        };

        mediaRecorder.onstop = () => {
            const blob = new Blob(chunks, { 'type': 'video/webm; codecs=vp9' });
            chunks = [];
            const formData = new FormData();
            formData.append('video', blob);

            fetch('/upload/', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const a = document.createElement('a');
                    a.href = data.downloadUrl;
                    a.textContent = 'Download your video';
                    document.body.appendChild(a);
                } else {
                    console.error('Upload failed');
                }
            });
        };
    })
    .catch(err => console.error('Error accessing media devices.', err));
