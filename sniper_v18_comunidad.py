# ==========================================================
# PROPIEDAD PRIVADA Y EXCLUSIVA DE VÍCTOR M. RIVERA
# SISTEMA SNIPER - MOTOR PRO-BLINDADO V18.1 (INTERFAZ EXCLUSIVA MÓVIL)
# FUNDACIÓN: 17/07/2025 (Versión Blanco y Negro V1.0)
# EVOLUCIÓN DOCUMENTADA: 2025-2026 (9 fotos + 4524 sorteos)
# AUTOR: Mente sin escuela, con terquedad de ingeniero.
# ESTE CÓDIGO ES DE USO EXCLUSIVO DEL AUTOR. PROHIBIDA SU DISTRIBUCIÓN.
# ==========================================================

from datetime import datetime, timedelta
import itertools
import os
import random
import webbrowser
from flask import Flask, jsonify, render_template_string, request
import numpy as np
import pandas as pd

app = Flask(__name__)

# ==========================================
# CONFIGURACIÓN DE FECHA REAL DE TU CSV
# ==========================================
FECHA_ULTIMO_SORTEO = "2026-08-03" 

# ==========================================
# PLANTILLA VISUAL MÓVIL EXCLUSIVA (DISEÑO VERTICAL MÓVIL)
# ==========================================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SISTEMA SNIPER V18.1 - VISTA MÓVIL</title>
    <style>
        :root {
            --bg-main: #05070a;
            --bg-card: #0d1117;
            --bg-header: #161b22;
            --accent-green: #00e676;
            --accent-blue: #38bdf8;
            --accent-purple: #a855f7;
            --text-main: #f0f6fc;
            --text-muted: #8b949e;
            --red-card: #7f1d1d;
            --green-card: #14532d;
            --blue-card: #1e3a8a;
        }
        body { 
            background-color: var(--bg-main); 
            color: var(--text-main); 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
            margin: 0; 
            padding: 0;
            display: flex;
            justify-content: center;
        }

        /* SIMULADOR DE PANTALLA DE CELULAR EN COMPUTADORA */
        .mobile-shell {
            width: 100%;
            max-width: 480px;
            background-color: #0d1117;
            min-height: 100vh;
            border-left: 2px solid #21262d;
            border-right: 2px solid #21262d;
            padding: 12px;
            box-sizing: border-box;
            box-shadow: 0 0 40px rgba(0,0,0,0.8);
        }

        .mobile-header {
            background: linear-gradient(180deg, #161b22 0%, #0d1117 100%);
            border: 1px solid #30363d;
            border-radius: 12px;
            padding: 12px;
            text-align: center;
            margin-bottom: 12px;
        }

        .badge-mobile-mode {
            background-color: rgba(0, 230, 118, 0.15);
            color: var(--accent-green);
            border: 1px solid var(--accent-green);
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 6px;
            letter-spacing: 1px;
        }

        .brand-title {
            font-size: 16px;
            font-weight: 800;
            color: #ffffff;
            margin: 0;
        }

        .firma-victor {
            font-size: 11px;
            font-weight: bold;
            background: linear-gradient(90deg, #38bdf8, #f43f5e, #facc15);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-top: 4px;
        }

        /* CONTROLES Y FILTROS EN MODALIDAD TÁCTIL */
        .control-group {
            display: flex;
            gap: 6px;
            margin-top: 10px;
            justify-content: center;
        }

        .btn-select {
            background-color: #21262d;
            color: #f0f6fc;
            border: 1px solid #30363d;
            padding: 8px;
            border-radius: 8px;
            font-size: 11px;
            font-weight: bold;
            flex: 1;
        }

        .btn-action-primary {
            background-color: var(--accent-purple);
            color: white;
            border: none;
            padding: 8px 12px;
            border-radius: 8px;
            font-weight: bold;
            font-size: 11px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            text-align: center;
        }

        .btn-vip-block {
            display: block;
            width: 100%;
            background-color: var(--accent-green);
            color: #000000;
            font-weight: 900;
            font-size: 13px;
            text-align: center;
            padding: 12px 0;
            border-radius: 10px;
            text-decoration: none;
            margin-top: 10px;
            box-shadow: 0 4px 15px rgba(0,230,118,0.3);
            box-sizing: border-box;
        }

        /* NAVEGACIÓN TIPO PESTAÑAS MÓVILES */
        .nav-scroller {
            display: flex;
            gap: 6px;
            overflow-x: auto;
            padding-bottom: 8px;
            margin-bottom: 12px;
        }

        .nav-scroller::-webkit-scrollbar { display: none; }

        .tab-btn {
            background-color: #21262d;
            color: var(--text-muted);
            padding: 8px 14px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: bold;
            text-decoration: none;
            white-space: nowrap;
            border: 1px solid #30363d;
        }

        .tab-btn.active {
            background-color: var(--accent-blue);
            color: #000000;
            border-color: var(--accent-blue);
        }

        /* BLOQUES MÓVILES */
        .card-block {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 12px;
            padding: 12px;
            margin-bottom: 12px;
        }

        .card-title {
            font-size: 12px;
            font-weight: bold;
            color: #f43f5e;
            text-transform: uppercase;
            margin-bottom: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .faltantes-box {
            background-color: #0d1117;
            border: 1px solid var(--accent-green);
            color: var(--accent-green);
            padding: 8px;
            border-radius: 8px;
            font-family: monospace;
            font-size: 14px;
            font-weight: bold;
            text-align: center;
            margin-top: 6px;
        }

        /* TARJETAS DE LAS 10 JUGADAS */
        .sniper-list { display: flex; flex-direction: column; gap: 8px; }
        .sniper-card {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            border-radius: 8px;
            font-family: monospace;
            font-weight: bold;
            font-size: 12px;
        }
        .sniper-card.red { background-color: var(--red-card); border-left: 4px solid #ef4444; }
        .sniper-card.green { background-color: var(--green-card); border-left: 4px solid #22c55e; }
        .sniper-card.blue { background-color: var(--blue-card); border-left: 4px solid #3b82f6; }

        /* TABLAS AJUSTADAS A MÓVIL */
        table { width: 100%; border-collapse: collapse; font-size: 11px; margin-top: 8px; }
        th, td { border: 1px solid #30363d; padding: 6px; text-align: center; }
        th { background-color: #21262d; color: var(--accent-blue); }

        .btn-mod-search {
            background-color: #21262d;
            color: var(--accent-blue);
            border: 1px solid #30363d;
            padding: 6px;
            border-radius: 6px;
            font-size: 10px;
            font-weight: bold;
            cursor: pointer;
            flex: 1;
        }
        .btn-mod-search.active {
            background-color: var(--accent-blue) !important;
            color: #000000 !important;
        }
    </style>
</head>
<body>

    <!-- MARCO CENTRAL MÓVIL -->
    <div class="mobile-shell">
        
        <!-- ENCABEZADO DESTACADO DE VERIFICACIÓN -->
        <div class="mobile-header">
            <span class="badge-mobile-mode">📱 MODO APP MÓVIL COMUNIDAD</span>
            <h1 class="brand-title">🎯 SISTEMA SNIPER V18.1</h1>
            <div class="firma-victor">Propiedad Sniper 🐍 Victor M. Rivera</div>
            
            <div class="control-group">
                <select class="btn-select" onchange="window.location.href='/?vista={{ vista }}&sub_vista={{ sub_vista }}&modo={{ modo }}&filtro_juego=' + this.value">
                    <option value="TODOS" {% if filtro_juego == 'TODOS' %}selected{% endif %}>Todos los Sorteos</option>
                    <option value="MEDIODIA" {% if filtro_juego == 'MEDIODIA' %}selected{% endif %}>Mediodía</option>
                    <option value="DE LAS TRES" {% if filtro_juego == 'DE LAS TRES' %}selected{% endif %}>De las Tres</option>
                    <option value="EXTRA" {% if filtro_juego == 'EXTRA' %}selected{% endif %}>Extra</option>
                    <option value="SIETE" {% if filtro_juego == 'SIETE' %}selected{% endif %}>De las Siete</option>
                    <option value="CLASICO" {% if filtro_juego == 'CLASICO' %}selected{% endif %}>Clásico</option>
                </select>

                <select class="btn-select" onchange="window.location.href='/?vista={{ vista }}&sub_vista={{ sub_vista }}&filtro_juego={{ filtro_juego }}&modo=' + this.value">
                    <option value="Hibrido" {% if modo == 'Hibrido' %}selected{% endif %}>Híbrido</option>
                    <option value="Conservador" {% if modo == 'Conservador' %}selected{% endif %}>Conservador</option>
                    <option value="Agresivo" {% if modo == 'Agresivo' %}selected{% endif %}>Agresivo</option>
                </select>

                <a href="/?vista={{ vista }}&sub_vista={{ sub_vista }}&modo={{ modo }}&filtro_juego={{ filtro_juego }}&recalcular=true" class="btn-action-primary">🔄</a>
            </div>

            <a href="/tarjeta_vip?filtro_juego={{ filtro_juego }}&modo={{ modo }}" target="_blank" class="btn-vip-block">
                📸 GENERAR TARJETA VIP
            </a>
        </div>

        <!-- PESTAÑAS DESLIZABLES EN CELULAR -->
        <div class="nav-scroller">
            <a href="/?vista=panel&modo={{ modo }}&filtro_juego={{ filtro_juego }}" class="tab-btn {% if vista == 'panel' %}active{% endif %}">📊 Panel</a>
            <a href="/?vista=desglose&modo={{ modo }}&filtro_juego={{ filtro_juego }}" class="tab-btn {% if vista == 'desglose' %}active{% endif %}">📋 Desglose</a>
            <a href="/?vista=auditoria&modo={{ modo }}&filtro_juego={{ filtro_juego }}" class="tab-btn {% if vista == 'auditoria' %}active{% endif %}">👁️ Auditoría</a>
            <a href="/?vista=backtesting&modo={{ modo }}&filtro_juego={{ filtro_juego }}" class="tab-btn {% if vista == 'backtesting' %}active{% endif %}">🔍 Backtesting</a>
            <a href="/?vista=cadena&sub_vista=cadena_fam&modo={{ modo }}&filtro_juego={{ filtro_juego }}" class="tab-btn {% if vista == 'cadena' %}active{% endif %}">🔗 Cadena</a>
        </div>

        <!-- CONTENIDO MÓVIL EN UNA SOLA COLUMNA -->
        {% if vista == 'panel' %}
        
        <div class="card-block">
            <div class="card-title">
                <span>🎯 DÍGITO FALTANTE P1-P5</span>
                <span style="color:var(--accent-green);">{{ total }} Sorteos</span>
            </div>
            <div class="faltantes-box">{{ verif|join('-') }}</div>
        </div>

        <div class="card-block">
            <div class="card-title" style="color:var(--accent-blue);">💰 MÉTRICAS ESTIMADAS</div>
            <div style="font-size:11px; display:flex; justify-content:space-around;">
                <span>D5: <b style="color:var(--accent-green);">{{ td5 }}</b></span>
                <span>C4: <b style="color:var(--accent-blue);">{{ tc4 }}</b></span>
                <span>T3: <b style="color:#facc15;">{{ tt3 }}</b></span>
            </div>
        </div>

        <div class="card-block">
            <div class="card-title">🎯 10 JUGADAS MAESTRAS SNIPER</div>
            <div class="sniper-list">
                {% for card in sniper_cards %}
                <div class="sniper-card {{ card.clase }}">
                    <div>
                        <div>{{ card.tipo }}</div>
                        <div style="font-size:14px; color:#ffffff;">{{ card.jugada }}</div>
                    </div>
                    <div style="text-align:right; font-size:10px; opacity:0.9;">
                        <div>{{ card.pts }} pts</div>
                        <div>D5:{{ card.d5 }} C4:{{ card.c4 }}</div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>

        <div class="card-block">
            <div class="card-title" style="color:#ef4444;">🔥 TOP 3 ATRASADOS X POSICIÓN</div>
            <div style="font-size:11px; font-family:monospace;">
                {% for p_txt in top_pos %}
                • {{ p_txt }}<br>
                {% endfor %}
            </div>
        </div>

        {% elif vista == 'desglose' %}
        <div class="card-block">
            <div class="card-title">📋 DESGLOSE DE JUGADAS</div>
            <table>
                <thead>
                    <tr>
                        <th>JUGADA</th>
                        <th>TERCIA</th>
                        <th>CUARTETA</th>
                        <th>DIRECTA 5</th>
                    </tr>
                </thead>
                <tbody>
                    {% for card in sniper_cards %}
                    <tr>
                        <td style="text-align:left; color:#f43f5e; font-weight:bold;">{{ card.tipo }}</td>
                        <td style="font-family:monospace;">{{ card.jugada[2:] }}</td>
                        <td style="font-family:monospace;">{{ card.jugada[1:] }}</td>
                        <td style="color:var(--accent-green); font-family:monospace; font-weight:bold;">{{ card.jugada }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>

        {% elif vista == 'auditoria' %}
        <div class="card-block">
            <div class="card-title" style="color:var(--accent-purple);">👁️ AUDITORÍA DE RENDIMIENTO</div>
            <table>
                <thead>
                    <tr>
                        <th>JUGADA</th>
                        <th>D5</th>
                        <th>C4</th>
                        <th>T3</th>
                        <th>FAM</th>
                    </tr>
                </thead>
                <tbody>
                    {% for card in sniper_cards %}
                    <tr>
                        <td style="text-align:left; font-weight:bold;">{{ card.tipo }}</td>
                        <td>{{ card.d5 }}</td>
                        <td>{{ card.c4 }}</td>
                        <td>{{ card.t3 }}</td>
                        <td><b>{{ card.fam }}</b></td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>

        {% elif vista == 'backtesting' %}
        <div class="card-block">
            <div class="card-title" style="color:var(--accent-green);">🔍 AUDITORÍA RETROACTIVA</div>
            <form action="/" method="GET" style="display:flex; gap:6px;">
                <input type="hidden" name="vista" value="backtesting">
                <input type="hidden" name="modo" value="{{ modo }}">
                <input type="hidden" name="filtro_juego" value="{{ filtro_juego }}">
                <input type="number" name="off" value="{{ off_val }}" class="btn-select" style="text-align:center;">
                <button type="submit" class="btn-action-primary">🔍 Ejecutar</button>
            </form>
            {% if bt_resultado %}
            <div style="background:#0d1117; padding:10px; border-radius:8px; margin-top:10px; font-size:11px;">
                <div style="color:var(--accent-blue); font-weight:bold;">🎯 {{ bt_resultado.off }} SORTEOS ATRÁS</div>
                <div>• Sorteo evaluado: #{{ bt_resultado.sorteo_evaluado }}</div>
                <div>• Combinación real: <b style="color:#facc15;">{{ bt_resultado.comb_real }}</b></div>
                <div>• Impactos -> D5: {{ bt_resultado.d5 }} | C4: {{ bt_resultado.c4 }} | T3: {{ bt_resultado.t3 }}</div>
            </div>
            {% endif %}
        </div>

        {% elif vista == 'cadena' %}
        <div class="nav-scroller" style="margin-bottom:8px;">
            <a href="/?vista=cadena&sub_vista=cadena_fam&modo={{ modo }}&filtro_juego={{ filtro_juego }}" class="tab-btn {% if sub_vista == 'cadena_fam' %}active{% endif %}">🔗 Cadena</a>
            <a href="/?vista=cadena&sub_vista=buscador&modo={{ modo }}&filtro_juego={{ filtro_juego }}" class="tab-btn {% if sub_vista == 'buscador' %}active{% endif %}">🔎 Busca</a>
        </div>

        {% if sub_vista == 'buscador' %}
        <div class="card-block">
            <div class="card-title" style="color:var(--accent-blue);">🔎 BUSCADOR FRENTE A HISTORIAL</div>
            
            <form action="/" method="GET" id="formBuscadorCadena">
                <input type="hidden" name="vista" value="cadena">
                <input type="hidden" name="sub_vista" value="buscador">
                <input type="hidden" name="modo" value="{{ modo }}">
                <input type="hidden" name="filtro_juego" value="{{ filtro_juego }}">
                <input type="hidden" id="mod_cifras_input" name="mod_cifras" value="{{ mod_cifras }}">

                <div style="display:flex; gap:4px; margin-bottom:8px; flex-wrap:wrap;">
                    <button type="button" class="btn-mod-search {% if mod_cifras == 1 %}active{% endif %}" onclick="seleccionarModBusca(1)">1D</button>
                    <button type="button" class="btn-mod-search {% if mod_cifras == 2 %}active{% endif %}" onclick="seleccionarModBusca(2)">2D</button>
                    <button type="button" class="btn-mod-search {% if mod_cifras == 3 %}active{% endif %}" onclick="seleccionarModBusca(3)">3D</button>
                    <button type="button" class="btn-mod-search {% if mod_cifras == 4 %}active{% endif %}" onclick="seleccionarModBusca(4)">4D</button>
                    <button type="button" class="btn-mod-search {% if mod_cifras == 5 %}active{% endif %}" onclick="seleccionarModBusca(5)">5D</button>
                </div>

                <div style="display:flex; gap:6px;">
                    <input type="text" id="comb_search_input" name="comb_search" value="{{ comb_search }}" class="btn-select" style="font-size:14px; text-align:center; font-weight:bold;" maxlength="{{ mod_cifras }}">
                    <button type="submit" class="btn-action-primary">Buscar</button>
                </div>
            </form>

            {% if ult_aparicion_info %}
            <div style="margin-top:10px; background:#0d1117; padding:8px; border-radius:6px; font-size:11px;">
                <div style="color:var(--accent-blue); font-weight:bold;">📌 ÚLTIMA APARICIÓN:</div>
                <div>• Fecha: <b style="color:var(--accent-green);">{{ ult_aparicion_info.fecha }}</b></div>
                <div>• Sorteo: {{ ult_aparicion_info.juego }} | Comb: <b style="color:#facc15;">{{ ult_aparicion_info.comb }}</b></div>
                <div>• Atraso: {{ ult_aparicion_info.atraso }} sorteos atrás</div>
            </div>
            {% endif %}
        </div>
        {% else %}
        <div class="card-block">
            <div class="card-title">🔗 CADENA DE FAMILIAS</div>
            <table>
                <thead>
                    <tr>
                        <th>FECHA 1</th>
                        <th>COMB 1</th>
                        <th>DÍAS</th>
                        <th>COMB 2</th>
                    </tr>
                </thead>
                <tbody>
                    {% for r in cadena_datos[:15] %}
                    <tr>
                        <td>{{ r.f1 }}</td>
                        <td style="color:var(--accent-blue); font-weight:bold;">{{ r.c1 }}</td>
                        <td style="color:#facc15;">{{ r.dias }}</td>
                        <td style="color:var(--accent-blue); font-weight:bold;">{{ r.c2 }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        {% endif %}
        {% endif %}

    </div>

    <script>
    function seleccionarModBusca(cifras) {
        document.getElementById('mod_cifras_input').value = cifras;
        let inp = document.getElementById('comb_search_input');
        inp.maxLength = cifras;
        if(inp.value.length > cifras) { inp.value = inp.value.slice(-cifras); }
        document.getElementById('formBuscadorCadena').submit();
    }
    </script>
</body>
</html>
"""

# ==========================================
# PLANTILLA HTML TARJETA VIP GENERADA
# ==========================================
TARJETA_VIP_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TARJETA VIP SNIPER V18.1 - {{ filtro_juego }}</title>
    <style>
        body { background-color: #0b0e14; color: #ffffff; font-family: sans-serif; margin: 0; padding: 10px; display: flex; justify-content: center; }
        .card-container { width: 100%; max-width: 480px; background: #121824; border: 2px solid #00e676; border-radius: 12px; padding: 16px; box-sizing: border-box; }
        .header { text-align: center; border-bottom: 2px solid #2a364f; padding-bottom: 10px; margin-bottom: 12px; }
        .header h1 { margin: 0; font-size: 18px; color: #00e676; }
        .fijas-container { background: rgba(255, 82, 82, 0.1); border: 1px solid #ff5252; border-radius: 8px; padding: 10px; text-align: center; margin-bottom: 15px; }
        .fija-badge { background: #ff5252; color: #ffffff; font-size: 18px; font-weight: bold; padding: 4px 12px; border-radius: 6px; font-family: monospace; }
        table { width: 100%; border-collapse: collapse; font-size: 11px; }
        th { background-color: #1e293b; color: #ffc107; padding: 8px 4px; }
        td { padding: 6px 4px; text-align: center; border-bottom: 1px solid #1e293b; font-family: monospace; }
    </style>
</head>
<body>
    <div class="card-container">
        <div class="header">
            <h1>🎯 GRUPO VIP SNIPER V18.1</h1>
            <p style="font-size:11px; color:#8a99ad;">Víctor M. Rivera | Pronóstico ({{ filtro_juego }})</p>
        </div>

        <div class="fijas-container">
            <div style="color:#ff5252; font-size:12px; font-weight:bold; margin-bottom:6px;">🔥 DIRECTAS FIJAS 🔥</div>
            <div style="display:flex; justify-content:center; gap:10px;">
                <div class="fija-badge">{{ fija_1 }}</div>
                <div class="fija-badge">{{ fija_2 }}</div>
            </div>
        </div>

        <table>
            <thead>
                <tr>
                    <th style="text-align:left;">Jugada</th>
                    <th>Directa 5</th>
                    <th>Cuarteta</th>
                    <th>Tercia</th>
                </tr>
            </thead>
            <tbody>
                {% for item in filas_tarjeta %}
                <tr>
                    <td style="text-align:left; color:#8a99ad;">{{ item.etiqueta }}</td>
                    <td style="color:#ffdd57; font-weight:bold;">{{ item.d5 }}</td>
                    <td>{{ item.d4 }}</td>
                    <td style="color:#00b0ff; font-weight:bold;">{{ item.d3 }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
"""

# ==========================================
# FUNCIONES AUXILIARES Y ANALÍTICAS (INTACTAS)
# ==========================================

def calcular_matriz_markov_posicional(df_completo):
    trans = {i: {d: [0]*10 for d in range(10)} for i in range(4)}
    if df_completo is None: return trans
    for fila in df_completo.values.tolist():
        digs = [int(x) for x in fila if str(x).isdigit()]
        if len(digs) >= 5:
            d5 = digs[-5:]
            for pos in range(4):
                trans[pos][d5[pos]][d5[pos+1]] += 1
    return trans

def aplicar_transicion_markov_cabeza(jugada_base, matriz_markov):
    if len(jugada_base) != 5 or not jugada_base.isdigit(): return jugada_base
    res = [int(c) for c in jugada_base]
    opciones = matriz_markov[0][res[0]]
    if sum(opciones) > 0:
        d_siguiente_prob = int(np.argmax(opciones))
        if opciones[d_siguiente_prob] > 2: res[1] = d_siguiente_prob
    return "".join(map(str, res))

def afinar_cabeza_gaussiana_p1_p2(jugada_5d, top3_15):
    if len(jugada_5d) != 5 or not jugada_5d.isdigit(): return jugada_5d
    digs = [int(c) for c in jugada_5d]
    suma = sum(digs)
    if suma > 27:
        for idx in [0, 1]:
            opciones = top3_15[idx]["atrasados"] + [top3_15[idx]["faltante"]]
            for d_alt in opciones:
                if d_alt < digs[idx]:
                    digs[idx] = d_alt
                    if 18 <= sum(digs) <= 27: return "".join(map(str, digs))
    elif suma < 18:
        for idx in [0, 1]:
            opciones = top3_15[idx]["frecuentes"] + top3_15[idx]["atrasados"]
            for d_alt in opciones:
                if d_alt > digs[idx]:
                    digs[idx] = d_alt
                    if 18 <= sum(digs) <= 27: return "".join(map(str, digs))
    return "".join(map(str, digs))

def forzar_coincidencia_familia_rotativa_p3_p5(jugada_5d, familias_maduras, indice_jugada):
    if not familias_maduras: return jugada_5d
    fam_elegida = familias_maduras[indice_jugada % len(familias_maduras)]
    return jugada_5d[:2] + "".join(sorted(list(fam_elegida)))

def obtener_familia_3d(comb_str):
    if not comb_str or len(str(comb_str)) < 3: return "000"
    return "".join(sorted(list(str(comb_str)[-3:])))

def tipo_familia_str(fam_3d):
    if len(set(fam_3d)) == 1: return "AAA"
    elif len(set(fam_3d)) == 2: return "AAB"
    return "ABC"

def obtener_datos_analisis(ruta_archivo, filtro_juego="TODOS"):
    try:
        lines = []
        juegos_ciclo = ["CLASICO", "SIETE", "EXTRA", "DE LAS TRES", "MEDIODIA"]
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                for idx_line, line in enumerate(f):
                    parts = [p.strip() for p in line.strip().split(',') if p.strip().isdigit()]
                    if len(parts) >= 5:
                        tipo_j = juegos_ciclo[idx_line % 5]
                        if filtro_juego == "TODOS" or tipo_j == filtro_juego:
                            lines.append(parts[-5:])
        df_completo = pd.DataFrame(lines)
        df = df_completo
        total = len(df)
        df_corto_15 = df.head(15)
        ultimos = ["".join([str(x) for x in fila[-5:]]) for fila in df_corto_15.values.tolist() if len(fila) >= 5][:15]
        verif = []
        top3_15 = []
        for i in range(5):
            col_vals = [int(fila[i]) for fila in df_corto_15.values.tolist() if len(fila) >= 5]
            col = pd.Series(col_vals)
            pond = {d: 0.0 for d in range(10)}
            for idx_w, v in enumerate(col):
                if v in pond: pond[v] += np.exp(-0.05 * idx_w)
            falt = sorted(pond.items(), key=lambda x: x[1])[0][0]
            verif.append(str(falt))
            top3_15.append({"faltante": falt, "atrasados": sorted(pond.keys(), key=lambda x: pond[x])[:3], "frecuentes": sorted(pond.keys(), key=lambda x: pond[x], reverse=True)[:3]})
        return ultimos, verif, total, df, top3_15, df_completo
    except Exception as e:
        return [], [], 0, None, [], None

def calcular_tipos_digitos(df):
    try:
        df_l = df.head(5000).copy()
        digs_todos = []
        for fila in df_l.values.tolist():
            d_row = [int(str(x)) for x in fila if pd.notna(x) and str(x).isdigit()]
            if len(d_row) >= 5: digs_todos.extend(d_row[-5:])
        c = pd.Series(digs_todos).value_counts().sort_index()
        for d in range(10):
            if d not in c: c[d] = 0
        return (c.nsmallest(3).index.tolist(), c.nlargest(3).index.tolist(), c.sort_values(ascending=False).iloc[3:6].index.tolist())
    except:
        return [0, 1, 2], [7, 8, 9], [3, 4, 5]

def obtener_familias_maduras_mes(df_completo):
    if df_completo is None: return [], []
    try:
        familias_conteo = {}; familias_ult = {}; idx = 0
        for fila in df_completo.values.tolist():
            digs = [str(x) for x in fila if pd.notna(x) and str(x).isdigit()]
            if len(digs) >= 5:
                comb = "".join(digs[-5:])
                fam = obtener_familia_3d(comb)
                familias_conteo[fam] = familias_conteo.get(fam, 0) + 1
                if fam not in familias_ult: familias_ult[fam] = idx
                idx += 1
                if idx >= 150: break
        maduras = [fam for fam, cnt in familias_conteo.items() if cnt == 1 and 3 <= familias_ult.get(fam, 0) <= 25]
        return sorted(maduras, key=lambda f: familias_ult.get(f, 0), reverse=True) if maduras else list(familias_conteo.keys())[:10], familias_ult
    except:
        return ["123", "456", "789"], {}

def generar_10_jugadas_sniper_afinadas(top3_15, frios, calientes, comunes, df_completo):
    GEM = {0: 5, 1: 6, 2: 7, 3: 8, 4: 9, 5: 0, 6: 1, 7: 2, 8: 3, 9: 4}
    F = [p["faltante"] for p in top3_15]
    A = [p["atrasados"][0] for p in top3_15]
    C = [p["frecuentes"][0] for p in top3_15]
    GF = [GEM[x] for x in F]; GA = [GEM[x] for x in A]
    familias_maduras, _ = obtener_familias_maduras_mes(df_completo)
    matriz_markov = calcular_matriz_markov_posicional(df_completo)
    j1 = "".join(map(str, F))
    j2 = "".join(map(str, [GEM[x] for x in A]))
    j3 = "".join(map(str, C))
    j4_frio = "".join(map(str, (frios * 3)[:5]))
    j5_comun = "".join(map(str, (comunes * 3)[:5]))
    j6_fac = f"{F[0]}{A[1]}{C[2]}{GF[3]}{GA[4]}"
    j7_acf = f"{A[0]}{C[1]}{F[2]}{GA[3]}{GF[4]}"
    j8_esc = f"{F[0]}{(F[0]+1)%10}{(F[0]+2)%10}{(F[0]+3)%10}{(F[0]+4)%10}"
    cand_afin = f"{F[0]}{C[1]}{A[2]}{C[3]}{F[4]}"
    cand_pool = f"{calientes[0]}{frios[0]}{comunes[0]}{calientes[1]}{frios[1]}"
    raw_base = [j1, j2, j3, j4_frio, j5_comun, j6_fac, j7_acf, j8_esc, cand_afin, cand_pool]
    etiquetas = ["1. F-FALTANTE", "2. A-ATRASADO", "3. C-CALIENTE", "4. F-FRIO", "5. M-COMUN","6. H1-FAC", "7. H2-ACF", "8. H3-ESCALERA", "9. SNIPER AFINADO", "10. SNIPER POOL INTEGRADO"]
    jugadas_finales = []
    for idx in range(10):
        code_markov = aplicar_transicion_markov_cabeza(raw_base[idx], matriz_markov)
        code_gauss = afinar_cabeza_gaussiana_p1_p2(code_markov, top3_15)
        code_final = forzar_coincidencia_familia_rotativa_p3_p5(code_gauss, familias_maduras, idx)
        pts_calibrado = 100 - (idx * 2)
        jugadas_finales.append([etiquetas[idx], code_final, pts_calibrado])
    return jugadas_finales

def calcular_auditoria_metricas_reales(jugadas_sniper, df_completo):
    if df_completo is None: return 0, 0, 0, []
    mat_rows = [int(str(x)) for fila in df_completo.values.tolist() for x in fila if pd.notna(x) and str(x).isdigit()]
    if not mat_rows: return 0, 0, 0, []
    mat_list = []
    for fila in df_completo.values.tolist():
        digs = [int(str(x)) for x in fila if pd.notna(x) and str(x).isdigit()]
        if len(digs) >= 5: mat_list.append(digs[-5:])
    if not mat_list: return 0, 0, 0, []
    mat = np.array(mat_list)
    td5 = tc4 = tt3 = 0; detalles = []
    for idx, (tipo, jugada, pts) in enumerate(jugadas_sniper):
        ja = np.array([int(d) for d in jugada if d.isdigit()])
        if len(ja) == 5:
            co = np.sum(mat == ja, axis=1)
            d5 = int(np.sum(co == 5)); c4 = int(np.sum(co == 4)); t3 = int(np.sum(co == 3))
            td5 += d5; tc4 += c4; tt3 += t3
            detalles.append({"d5": d5, "c4": c4, "t3": t3})
        else: detalles.append({"d5": 0, "c4": 0, "t3": 0})
    return td5, tc4, tt3, detalles

# ==========================================
# ENDPOINT TARJETA VIP
# ==========================================
@app.route("/tarjeta_vip")
def tarjeta_vip():
    filtro_juego = request.args.get("filtro_juego", "TODOS")
    ruta = "tris_historial.csv"
    ultimos, verif, total, df, top3_15, df_completo = obtener_datos_analisis(ruta, filtro_juego)
    if df is None: return "Error al cargar los datos."
    frios, calientes, comunes = calcular_tipos_digitos(df)
    jugadas_sniper = generar_10_jugadas_sniper_afinadas(top3_15, frios, calientes, comunes, df_completo)
    filas_tarjeta = [{"etiqueta": tipo, "d5": jugada, "d4": jugada[1:], "d3": jugada[2:]} for tipo, jugada, pts in jugadas_sniper]
    return render_template_string(TARJETA_VIP_TEMPLATE, filtro_juego=filtro_juego, fija_1=jugadas_sniper[0][1], fija_2=jugadas_sniper[1][1], filas_tarjeta=filas_tarjeta)

# ==========================================
# ENDPOINT PRINCIPAL (PUERTO 5000 INDEPENDIENTE)
# ==========================================
@app.route("/")
def index():
    modo = request.args.get("modo", "Hibrido")
    vista = request.args.get("vista", "panel")
    sub_vista = request.args.get("sub_vista", "cadena_fam")
    filtro_juego = request.args.get("filtro_juego", "TODOS")
    off_val = request.args.get("off", 50, type=int)
    comb_search = request.args.get("comb_search", "04277").strip()
    mod_cifras = request.args.get("mod_cifras", 5, type=int)

    ruta = "tris_historial.csv"
    ultimos, verif, total, df, top3_15, df_completo = obtener_datos_analisis(ruta, filtro_juego)
    if df is None: return "Error al cargar los datos."
        
    frios, calientes, comunes = calcular_tipos_digitos(df)
    jugadas_sniper = generar_10_jugadas_sniper_afinadas(top3_15, frios, calientes, comunes, df_completo)
    familias_maduras, _ = obtener_familias_maduras_mes(df_completo)
    td5_real, tc4_real, tt3_real, detalles_aud = calcular_auditoria_metricas_reales(jugadas_sniper, df_completo)
    
    sniper_cards = []
    for idx, (tipo, jugada, pts) in enumerate(jugadas_sniper):
        fam = obtener_familia_3d(jugada)
        aud = detalles_aud[idx] if idx < len(detalles_aud) else {}
        clase_color = "red" if idx < 3 else ("green" if idx < 7 else "blue")
        sniper_cards.append({"tipo": tipo, "jugada": jugada, "pts": pts, "fam": fam, "clase": clase_color, "d5": aud.get("d5", 0), "c4": aud.get("c4", 0), "t3": aud.get("t3", 0)})
    
    top_pos = [f"P{i+1}: F={top3_15[i]['faltante']} A={top3_15[i]['atrasados'][0]} C={top3_15[i]['frecuentes'][0]}" for i in range(5)]
    
    bt_resultado = None
    if vista == 'backtesting' and off_val > 0 and len(df_completo) > off_val:
        row_eval = df_completo.iloc[off_val - 1].values.tolist()
        bt_resultado = {"off": off_val, "sorteo_evaluado": total - off_val + 1, "comb_real": "".join([str(x) for x in row_eval[-5:]]), "d5": 0, "c4": 0, "t3": 0}
    
    cadena_datos = []; filas_procesadas = []
    juegos_ciclo = ["CLASICO", "SIETE", "EXTRA", "DE LAS TRES", "MEDIODIA"]
    DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    try: fecha_referencia_base = datetime.strptime(FECHA_ULTIMO_SORTEO, "%Y-%m-%d")
    except: fecha_referencia_base = datetime(2026, 8, 3)

    if os.path.exists(ruta):
        with open(ruta, 'r', encoding='utf-8') as f:
            for idx_row, line in enumerate(f):
                parts = [p.strip() for p in line.strip().split(',') if p.strip().isdigit()]
                if len(parts) >= 5:
                    dias_atras = idx_row // 5
                    fecha_real = fecha_referencia_base - timedelta(days=dias_atras)
                    filas_procesadas.append({"idx": idx_row, "fecha": fecha_real.strftime("%Y-%m-%d"), "juego": juegos_ciclo[idx_row % 5], "comb": "".join(parts[-5:]), "fam": obtener_familia_3d("".join(parts[-5:]))})
            
    if vista == 'cadena' and sub_vista == 'cadena_fam':
        familias_map = {}
        for f_item in filas_procesadas:
            familias_map.setdefault(f_item["fam"], []).append(f_item)
        for fam, app_list in familias_map.items():
            if len(app_list) >= 2:
                for i in range(len(app_list) - 1):
                    cadena_datos.append({"f1": app_list[i+1]["fecha"], "c1": app_list[i+1]["comb"], "dias": abs(app_list[i+1]["idx"] - app_list[i]["idx"]), "c2": app_list[i]["comb"]})
                    if len(cadena_datos) >= 200: break
            if len(cadena_datos) >= 200: break
            
    res_search = []; ult_aparicion_info = None
    if sub_vista == 'buscador' and comb_search:
        term_base = comb_search[-mod_cifras:]
        coincidencias = [f for f in filas_procesadas if f["comb"].endswith(term_base)]
        if coincidencias:
            ult_aparicion_info = {"fecha": coincidencias[0]["fecha"], "juego": coincidencias[0]["juego"], "comb": coincidencias[0]["comb"], "atraso": coincidencias[0]["idx"]}

    return render_template_string(
        HTML_TEMPLATE, 
        total=total, ultimos=ultimos, verif=verif, top_pos=top_pos, frios=frios, calientes=calientes, comunes=comunes, 
        sniper_cards=sniper_cards, td5=td5_real, tc4=tc4_real, tt3=tt3_real, modo=modo, vista=vista, sub_vista=sub_vista, 
        filtro_juego=filtro_juego, off_val=off_val, comb_search=comb_search, mod_cifras=mod_cifras, res_search=res_search, 
        ult_aparicion_info=ult_aparicion_info, cadena_datos=cadena_datos, bt_resultado=bt_resultado
    )

if __name__ == "__main__":
    try:
        webbrowser.open("http://127.0.0.1:5000/")
    except:
        pass
        
    app.run(host="0.0.0.0", port=5000, debug=False)