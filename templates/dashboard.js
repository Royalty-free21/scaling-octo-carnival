async function fetchVitals() {
  try {
    const res = await fetch('/api/patient');
    const data = await res.json();
    document.getElementById('vitals-content').innerHTML = `
      <b>Patient ID:</b> ${data.patient_id}<br>
      <b>Heart Rate:</b> ${data.heart_rate} bpm<br>
      <b>SpO2:</b> ${data.spo2}%<br>
      <b>BP:</b> ${data.blood_pressure_systolic}/${data.blood_pressure_diastolic} mmHg<br>
      <b>Temp:</b> ${data.temperature_c} °C<br>
      <b>ECG Score:</b> ${data.ecg_alert_score}<br>
    `;
    document.getElementById('network-content').innerHTML = `
      <b>Latency:</b> ${data.latency_ms} ms<br>
      <b>Packet Loss:</b> ${(data.packet_loss_pct*100).toFixed(3)}%<br>
      <b>Bandwidth:</b> ${data.bandwidth_gbps} Gbps<br>
    `;
  } catch(e) {
    console.error(e);
  }
}

document.getElementById('send').addEventListener('click', async () => {
  const cmd = document.getElementById('cmd').value || 'cut';
  document.getElementById('robot-response').innerText = 'Sending...';
  const res = await fetch(`/api/surgery/${encodeURIComponent(cmd)}`);
  const j = await res.json();
  document.getElementById('robot-response').innerHTML = `
    <b>Cmd:</b> ${j.command_received} <br>
    <b>Action:</b> ${j.robot_action} <br>
    <b>Latency:</b> ${j.network_latency_ms} ms <br>
    <b>Accuracy:</b> ${j.precision_accuracy}%
  `;
});

// refresh periodically
fetchVitals();
setInterval(fetchVitals, 1500);
