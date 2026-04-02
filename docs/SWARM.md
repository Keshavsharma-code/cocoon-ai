# 🐝 Swarm Protocol: Distributed Mode

Cocoon isn't limited to a single machine. The swarm can coordinate across heterogeneous environments.

## Orchestration Tiers
1. **Local Swarm**: Mother + Hive on one machine.
2. **Cloud Swarm**: Mother orchestrating remote Hive runtimes (via the `web` crate).
3. **P2P Swarm**: Collaborative metamorphosis between multiple Mothers (Experimental).

## Security
- All inter-agent communication is encrypted via the `crypto` utility.
- Larvae are authenticated before joining the silk-thread log.
