from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class TrainingConfig:
    output_dir: str = "models"
    total_timesteps: int = 1_000_000
    n_envs: int = 8
    seed: int = 42
    resume_from: str | None = None
    use_rerun: bool = False


@dataclass
class CurriculumStageConfig:
    name: str = "stage"
    total_timesteps: int = 100_000
    waypoint_noise: float | None = None
    add_sensor_noise: bool | None = None
    random_start_waypoint: bool | None = None
    max_waypoints: int | None = None
    max_episode_steps: int | None = None
    action_scale: float | None = None
    random_start_position: bool | None = None
    start_position_noise: float | None = None


@dataclass
class CurriculumConfig:
    enabled: bool = False
    stages: list[CurriculumStageConfig] = field(default_factory=list)


@dataclass
class NetArchConfig:
    pi: list[int] = field(default_factory=lambda: [256, 256])
    vf: list[int] = field(default_factory=lambda: [256, 256])


@dataclass
class PPOConfig:
    learning_rate: float = 3e-4
    batch_size: int = 256
    n_steps: int = 2048
    n_epochs: int = 10
    gamma: float = 0.99
    gae_lambda: float = 0.95
    clip_range: float = 0.2
    ent_coef: float = 0.01
    vf_coef: float = 0.5
    max_grad_norm: float = 0.5
    net_arch: NetArchConfig = field(default_factory=NetArchConfig)


@dataclass
class VecNormalizeConfig:
    norm_obs: bool = False
    norm_reward: bool = True
    clip_obs: float = 10.0
    clip_reward: float = 10.0
    eval_norm_reward: bool = False


@dataclass
class EnvConfig:
    waypoint_radius: float = 1.0
    waypoint_noise: float = 1.0
    waypoint_yaw_random: bool = True
    max_episode_steps: int = 5000
    arena_size: float = 25.0
    max_altitude: float = 10.0
    max_tilt_angle: float = 1.4
    disable_tilt_termination: bool = False
    goal_max_distance: float = 12.0
    include_position: bool = False
    random_start_waypoint: bool = False
    add_sensor_noise: bool = True
    max_waypoints: int | None = None
    action_scale: float = 1.0
    random_start_position: bool = False
    start_position_noise: float = 0.0
    speed_normalization: float = 5.0
    bounds_margin: float = 5.0
    ground_threshold: float = 0.05
    timestep: float = 0.01


@dataclass
class RewardConfig:
    progress_multiplier: float = 5.0
    time_penalty: float = 0.01
    waypoint_bonus: float = 50.0
    path_complete_bonus: float = 100.0
    completion_time_divisor: float = 100.0
    close_proximity_3x_bonus: float = 0.1
    close_proximity_3x_radius: float = 3.0
    close_proximity_1_5x_bonus: float = 0.2
    close_proximity_1_5x_radius: float = 1.5
    collision_penalty: float = 10.0
    tilt_penalty: float = 10.0
    out_of_bounds_penalty: float = 5.0


@dataclass
class QuadcopterConfig:
    mass: float = 0.5
    arm_length: float = 0.17
    thrust_to_weight: float = 2.0
    inertia: tuple[float, float, float] = (0.0023, 0.0023, 0.004)
    drag_coeff: float = 0.01
    motor_time_constant: float = 0.02


@dataclass
class SensorConfig:
    accel_noise_std: float = 0.1
    accel_bias_std: float = 0.02
    accel_bias_time_constant: float = 100.0
    gyro_noise_std: float = 0.01
    gyro_bias_std: float = 0.001
    gyro_bias_time_constant: float = 100.0
    position_noise_std: float = 0.01
    velocity_noise_std: float = 0.05


@dataclass
class CallbackConfig:
    checkpoint_freq: int = 50_000
    eval_freq: int = 10_000
    n_eval_episodes: int = 5
    log_3d_freq: int = 3
    summary_update_freq: int = 10


@dataclass
class EvaluationEnvConfig:
    waypoint_noise: float = 0.0
    waypoint_yaw_random: bool = False
    include_position: bool = False
    add_sensor_noise: bool = True
    disable_tilt_termination: bool = True


@dataclass
class EvaluationConfig:
    realtime: bool = True
    slow_motion: float = 1.0
    env: EvaluationEnvConfig = field(default_factory=EvaluationEnvConfig)


@dataclass
class DemoEnvConfig:
    waypoint_noise: float = 1.0
    waypoint_yaw_random: bool = True
    include_position: bool = False
    add_sensor_noise: bool = True
    disable_tilt_termination: bool = False


@dataclass
class DemoConfig:
    max_steps: int = 500
    sleep_time: float = 0.01
    env: DemoEnvConfig = field(default_factory=DemoEnvConfig)


@dataclass
class VisualizationConfig:
    training_app_id: str = "simhops-training"
    eval_app_id: str = "simhops-eval"
    demo_app_id: str = "simhops-demo"
    spawn: bool = True


@dataclass
class SimHopsConfig:
    training: TrainingConfig = field(default_factory=TrainingConfig)
    curriculum: CurriculumConfig = field(default_factory=CurriculumConfig)
    ppo: PPOConfig = field(default_factory=PPOConfig)
    vecnormalize: VecNormalizeConfig = field(default_factory=VecNormalizeConfig)
    env: EnvConfig = field(default_factory=EnvConfig)
    reward: RewardConfig = field(default_factory=RewardConfig)
    quadcopter: QuadcopterConfig = field(default_factory=QuadcopterConfig)
    sensor: SensorConfig = field(default_factory=SensorConfig)
    callbacks: CallbackConfig = field(default_factory=CallbackConfig)
    evaluation: EvaluationConfig = field(default_factory=EvaluationConfig)
    demo: DemoConfig = field(default_factory=DemoConfig)
    visualization: VisualizationConfig = field(default_factory=VisualizationConfig)


def deep_merge(base: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    for key, value in overrides.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            base[key] = deep_merge(base[key], value)
        else:
            base[key] = value
    return base


def build_config(data: dict[str, Any]) -> SimHopsConfig:
    curriculum_data = data.get("curriculum", {})
    stages_data = curriculum_data.get("stages", [])
    stages = [CurriculumStageConfig(**stage) for stage in stages_data]

    return SimHopsConfig(
        training=TrainingConfig(**data["training"]),
        curriculum=CurriculumConfig(
            enabled=curriculum_data.get("enabled", False),
            stages=stages,
        ),
        ppo=PPOConfig(
            learning_rate=data["ppo"]["learning_rate"],
            batch_size=data["ppo"]["batch_size"],
            n_steps=data["ppo"]["n_steps"],
            n_epochs=data["ppo"]["n_epochs"],
            gamma=data["ppo"]["gamma"],
            gae_lambda=data["ppo"]["gae_lambda"],
            clip_range=data["ppo"]["clip_range"],
            ent_coef=data["ppo"]["ent_coef"],
            vf_coef=data["ppo"]["vf_coef"],
            max_grad_norm=data["ppo"]["max_grad_norm"],
            net_arch=NetArchConfig(**data["ppo"]["net_arch"]),
        ),
        vecnormalize=VecNormalizeConfig(**data["vecnormalize"]),
        env=EnvConfig(**data["env"]),
        reward=RewardConfig(**data["reward"]),
        quadcopter=QuadcopterConfig(
            mass=data["quadcopter"]["mass"],
            arm_length=data["quadcopter"]["arm_length"],
            thrust_to_weight=data["quadcopter"]["thrust_to_weight"],
            inertia=tuple(data["quadcopter"]["inertia"]),
            drag_coeff=data["quadcopter"]["drag_coeff"],
            motor_time_constant=data["quadcopter"]["motor_time_constant"],
        ),
        sensor=SensorConfig(**data["sensor"]),
        callbacks=CallbackConfig(**data["callbacks"]),
        evaluation=EvaluationConfig(
            realtime=data["evaluation"]["realtime"],
            slow_motion=data["evaluation"]["slow_motion"],
            env=EvaluationEnvConfig(**data["evaluation"]["env"]),
        ),
        demo=DemoConfig(
            max_steps=data["demo"]["max_steps"],
            sleep_time=data["demo"]["sleep_time"],
            env=DemoEnvConfig(**data["demo"]["env"]),
        ),
        visualization=VisualizationConfig(**data["visualization"]),
    )


def resolve_config_path(path: Path) -> Path:
    if path.exists():
        return path
    fallback = Path(__file__).resolve().parents[3] / "cfg_default.yaml"
    if path.name == "cfg_default.yaml" and fallback.exists():
        return fallback
    raise FileNotFoundError(f"Config file not found: {path}")


def load_config(path: Path) -> tuple[SimHopsConfig, dict[str, Any]]:
    path = resolve_config_path(path)
    with path.open("r", encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}

    defaults = asdict(SimHopsConfig())
    merged = deep_merge(defaults, raw)
    return build_config(merged), merged
