class VoiceTelephonyBargeinInterruptionCoordinatorClient:
    def coordinate_bargein(self, caller_audio_energy_db=-18.5, bot_is_speaking=True, min_bargein_duration_ms=180):
        interrupted = caller_audio_energy_db > -25.0 and bot_is_speaking
        return {
            'coordination_id': 'brg_cor_9918',
            'bargein_detected': interrupted,
            'interruption_latency_ms': 42,
            'tts_playback_halt_signal': interrupted,
            'conversation_state': 'TRANSITION_TO_LISTEN',
            'unheard_audio_buffered_ms': 120,
            'telemetry_stream_url': 'https://bland.voice.genpark.ai/bargein/9918.json'
        }
