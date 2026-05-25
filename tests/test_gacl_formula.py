from src.methods.gacl import GACLConfig, apply_gacl


def test_gacl_interpolates_toward_reference_when_gate_fires():
    joint = {"audio": -2.0, "text": 0.0}
    ref = {"audio": 0.0, "text": -2.0}
    out = apply_gacl(joint, ref, GACLConfig(lambda_value=1.0, tau_A=0.5))
    assert out["N_out"] == 1
    assert out["alpha"] == 1.0
    assert out["gacl_answer"] == "audio"


def test_gacl_preserves_joint_when_reference_agrees():
    joint = {"audio": 0.0, "text": -1.0}
    ref = {"audio": 0.0, "text": -2.0}
    out = apply_gacl(joint, ref, GACLConfig(lambda_value=1.0, tau_A=0.5))
    assert out["N_out"] == 0
    assert out["alpha"] == 0.0
    assert out["gacl_answer"] == "audio"
