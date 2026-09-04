from client import VoiceTelephonyBargeinInterruptionCoordinatorClient

def main():
    client = VoiceTelephonyBargeinInterruptionCoordinatorClient()
    res = client.coordinate_bargein(-15.0, True)
    print('Barge-in Coordinator: ' + res['coordination_id'] + ' (Interrupted: ' + str(res['bargein_detected']) + ')')
    print('Halt Signal: ' + str(res['tts_playback_halt_signal']) + ' | Latency: ' + str(res['interruption_latency_ms']) + 'ms')
    print('Stream URL: ' + res['telemetry_stream_url'])

if __name__ == '__main__':
    main()
