import os
import sys
import time
import asyncio
import secrets
from datetime import datetime

# ==========================================
# AGNI-ALERT: SOLAR FLARE 20-COLOR PALETTE
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;196m', '\033[38;5;208m', '\033[38;5;226m', '\033[38;5;244m', '\033[38;5;255m'
C6, C7, C8, C9, C10  = '\033[38;5;39m', '\033[38;5;232m', '\033[38;5;201m', '\033[38;5;52m', '\033[38;5;118m'
C11, C12, C13, C14, C15 = '\033[38;5;130m', '\033[38;5;166m', '\033[38;5;214m', '\033[38;5;240m', '\033[38;5;153m'
C16, C17, C18, C19, C20 = '\033[38;5;124m', '\033[38;5;160m', '\033[38;5;88m', '\033[38;5;197m', '\033[38;5;215m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE BURNING FLAME
# ==========================================
async def agni_ignition_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C1}          (  )   (  )
    {C2}         (    ) (    )
    {C17}        (      ^      )
    {C12}         (    {C13}AGNI{C12}    )
    {C11}          (   {C3}v3.6{C11}   )
    {C9}           '-------'
    """
    print(logo)
    print(f"{C1}{BLD}   AGNI-ALERT: REAL-TIME VIOLATION INTERRUPT{RST}\n")
    
    # Heatwave animation
    waves = [C1, C17, C12, C2, C13, C3]
    for i in range(10):
        color = waves[i % len(waves)]
        sys.stdout.write(f"\r{C14}[*] Calibrating Thermal Sensors... {color}{'~' * (i+1)}{RST}")
        sys.stdout.flush()
        await asyncio.sleep(0.1)
    print(f"\n{C10}[+] Sensors Ignited. Monitoring High-Priority Breach Signals.{RST}\n")

# ==========================================
# ARCHITECTURE: ASYNC PRIORITY DISPATCHER
# ==========================================
class AgniDispatcher:
    """Handles alerts based on weight/priority using an Async Queue."""
    def __init__(self):
        self.queue = asyncio.PriorityQueue()

    async def push_event(self, priority, source, msg):
        """Higher priority = Lower number (0 is highest)."""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        await self.queue.put((priority, timestamp, source, msg))

    async def alert_monitor(self):
        """Asynchronously waits and flashes alerts based on priority."""
        while True:
            priority, ts, src, msg = await self.queue.get()
            
            # Formatting based on severity
            if priority == 0: # CRITICAL BREACH
                color, prefix = C1, f"{C7}{C1}!!! CRITICAL VIOLATION !!!{RST}"
                border = f"{C1}█{RST}"
            elif priority == 1: # HIGH RISK
                color, prefix = C17, f"{C17}!! HIGH RISK ALERT !!{RST}"
                border = f"{C17}▓{RST}"
            else: # MODERATE
                color, prefix = C12, f"! WARNING !"
                border = f"{C12}▒{RST}"

            print(f"\n{border} {prefix}")
            print(f"{border} {C14}TIME   : {C5}{ts}{RST}")
            print(f"{border} {C14}SOURCE : {C13}{src}{RST}")
            print(f"{border} {C14}MESSAGE: {color}{msg}{RST}")
            print(f"{border} {'━'*40}{RST}")
            
            await asyncio.sleep(0.1) # Rapid processing
            self.queue.task_done()

# ==========================================
# SIMULATED ENVIRONMENT
# ==========================================
async def simulate_system_load(dispatcher):
    """Simulates background noise and sudden spikes in violations."""
    sources = ["NETWORK_GATE", "CUI_VAULT_01", "USER_AUTH_L3", "KERNEL_API"]
    
    # Sequence of events: Mixed priorities
    events = [
        (2, 0, "Unauthorized directory listing attempt"),
        (2, 1, "Password retry detected"),
        (0, 3, "CUI_DATA_EXFILTRATION: Bulk transfer to foreign IP"), # THE BIG BREACH
        (1, 2, "Root shell privilege escalation attempt"),
        (2, 0, "Insecure protocol usage"),
        (0, 1, "PHYSICAL_TAMPER: Hardware enclosure opened") # ANOTHER CRITICAL
    ]

    for prio, src_idx, msg in events:
        await asyncio.sleep(secrets.randbelow(3) + 1)
        await dispatcher.push_event(prio, sources[src_idx], msg)

async def main():
    await agni_ignition_anim()
    dispatcher = AgniDispatcher()

    # Start the monitor and the simulator concurrently
    try:
        await asyncio.gather(
            dispatcher.alert_monitor(),
            simulate_system_load(dispatcher)
        )
    except asyncio.CancelledError:
        pass

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{C1}[!] Flame extinguished. Monitoring halted.{RST}")