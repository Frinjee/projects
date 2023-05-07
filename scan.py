import subprocess

def run_bandit():
    result = subprocess.run(['bandit', '-r', '.'], capture_output=True, text=True)
    if result.returncode != 0:
        print('Security scan failed:')
        print(result.stdout)
        raise SystemExit(1)
    else:
        print('Security scan passed:')
        print(result.stdout)

if __name__ == '__main__':
    run_bandit()
