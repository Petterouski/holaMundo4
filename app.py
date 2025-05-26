import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return '''
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Dev hola mundeishion DevOps con Heroku</title>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
            <style>
                :root {
                    --primary: #6c5ce7;
                    --secondary: #a29bfe;
                    --dark: #2d3436;
                    --light: #f5f6fa;
                    --google: #4285F4;
                }
                body {
                    font-family: 'Roboto', sans-serif;
                    background: linear-gradient(135deg, var(--light) 0%, #dfe6e9 100%);
                    margin: 0;
                    padding: 0;
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    color: var(--dark);
                }
                .container {
                    background: white;
                    border-radius: 16px;
                    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
                    width: 85%;
                    max-width: 800px;
                    padding: 40px;
                    text-align: center;
                    position: relative;
                    overflow: hidden;
                }
                .container::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 8px;
                    background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%);
                }
                h1 {
                    color: var(--primary);
                    margin-bottom: 24px;
                    font-weight: 500;
                }
                .devops-badge {
                    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
                    color: white;
                    display: inline-block;
                    padding: 8px 16px;
                    border-radius: 50px;
                    font-size: 14px;
                    margin-bottom: 24px;
                    font-weight: 500;
                }
                .content-box {
                    background: var(--light);
                    border-radius: 12px;
                    padding: 20px;
                    margin: 24px 0;
                    text-align: left;
                    border-left: 4px solid var(--primary);
                }
                .highlight {
                    color: var(--primary);
                    font-weight: 500;
                }
                .button-group {
                    display: flex;
                    justify-content: center;
                    gap: 15px;
                    flex-wrap: wrap;
                    margin-top: 20px;
                }
                button {
                    background: var(--primary);
                    color: white;
                    border: none;
                    padding: 12px 28px;
                    font-size: 16px;
                    border-radius: 50px;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    font-weight: 500;
                    letter-spacing: 0.5px;
                    min-width: 200px;
                }
                button:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 4px 12px rgba(108, 92, 231, 0.3);
                }
                .btn-primary {
                    background: var(--primary);
                }
                .btn-primary:hover {
                    background: var(--secondary);
                }
                .btn-google {
                    background: var(--google);
                }
                .btn-google:hover {
                    background: #3367d6;
                }
                .features {
                    display: flex;
                    justify-content: space-around;
                    flex-wrap: wrap;
                    margin: 32px 0;
                }
                .feature {
                    width: 30%;
                    min-width: 200px;
                    margin: 10px;
                    padding: 15px;
                    background: white;
                    border-radius: 8px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
                }
                .feature-icon {
                    font-size: 24px;
                    margin-bottom: 12px;
                    color: var(--primary);
                }
                .feature h3 {
                    margin-top: 0;
                    color: var(--dark);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 DevOps en Acción</h1>
                <div class="devops-badge">CI/CD con Heroku</div>
                
                <div class="content-box">
                    <p>Este proyecto demuestra la implementación de <span class="highlight">Integración Continua (CI)</span> y <span class="highlight">Despliegue Continuo (CD)</span> usando Heroku.</p>
                    <p>El 20% clave: Heroku automatiza el despliegue cuando detecta cambios en el repositorio, permitiendo entregas rápidas y consistentes.</p>
                </div>
                
                <div class="features">
                    <div class="feature">
                        <div class="feature-icon">🔁</div>
                        <h3>Integración Continua</h3>
                        <p>Pruebas automáticas con cada cambio en el código.</p>
                    </div>
                    <div class="feature">
                        <div class="feature-icon">⚡</div>
                        <h3>Despliegue Continuo</h3>
                        <p>Actualizaciones automáticas en producción.</p>
                    </div>
                    <div class="feature">
                        <div class="feature-icon">🔒</div>
                        <h3>Seguridad</h3>
                        <p>Procesos estandarizados y auditables.</p>
                    </div>
                </div>
                
                <div class="button-group">
                    <button class="btn-primary" onclick="window.location.href='https://front-paas-production.up.railway.app/'">
                        Proyecto Principal
                    </button>
                    <button class="btn-google" onclick="window.location.href='https://www.google.com'">
                        Buscar en Google
                    </button>
                </div>
            </div>
        </body>
        </html>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)