const { exec } = require('child_process');

// 启动 Astro 项目
const startAstro = exec('npm run dev', { cwd: '/work/python/finance/frontend' });
startAstro.stdout.on('data', (data) => {
  console.log(`Astro: ${data}`);
});

startAstro.stderr.on('data', (data) => {
  console.error(`Astro error: ${data}`);
});

// 启动 Python 项目
const startPython = exec('python app.py', { cwd: '/work/python/finance/backend' });
startPython.stdout.on('data', (data) => {
  console.log(`Python: ${data}`);
});

startPython.stderr.on('data', (data) => {
  console.error(`Python error: ${data}`);
});

console.log('Astro 和 Python 项目已启动。');
