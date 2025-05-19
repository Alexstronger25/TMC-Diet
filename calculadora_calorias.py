def calcular_cbm(peso_kg, altura_cm, edad_anos, genero):
    if genero == 'masculino':
        return 10 * peso_kg + 6.25 * altura_cm - 5 * edad_anos + 5
    elif genero == 'femenino':
        return 10 * peso_kg + 6.25 * altura_cm - 5 * edad_anos - 161
    else:
        raise ValueError("Genero no reconocido")

def calcular_aftd(cbm, nivel_actividad):
    factores_actividad = {
        'sedentario': 1.2,
        'ligera': 1.375,
        'moderada': 1.55,
        'alta': 1.725,
        'muy_alta': 1.9
    }
    return cbm * factores_actividad[nivel_actividad]

def calcular_ctn(aftd, objetivo):
    ajustes_caloricas = {
        'perder_grasa': -400,
        'mantener': 0,
        'ganar_muscular': 400
    }
    return aftd + ajustes_caloricas[objetivo]

def calcular_macronutrientes(peso_kg, objetivo):
    macronutrientes = {
        'perder_grasa': {'proteinas': 2.5, 'carbohidratos': 2.5, 'grasas': 1.0},
        'mantener': {'proteinas': 2.0, 'carbohidratos': 3.5, 'grasas': 1.0},
        'ganar_muscular': {'proteinas': 3.0, 'carbohidratos': 4.5, 'grasas': 1.0}
    }
    macronutrientes_objetivo = macronutrientes[objetivo]
    return {
        'proteinas': macronutrientes_objetivo['proteinas'] * peso_kg,
        'carbohidratos': macronutrientes_objetivo['carbohidratos'] * peso_kg,
        'grasas': macronutrientes_objetivo['grasas'] * peso_kg
    }

def ajustar_calorías_semanalmente(calorias_actuales, peso_perdido):
    ajustes = {
        'perder_grasa': {
            '>0.5': -150,
            '<0.5': 0
        },
        'mantener': {
            '>0': -150,
            '<0': 150
        },
        'ganar_muscular': {
            '>0.5': 0,
            '<0': -150
        }
    }
    # Asumimos que el objetivo es perder grasa
    if peso_perdido > 0.5:
        return calorias_actuales + ajustes['perder_grasa']['>0.5']
    else:
        return calorias_actuales + ajustes['perder_grasa']['<0.5']

# Ejemplo de uso
peso_kg = 85
altura_cm = 180
edad_anos = 30
genero = 'masculino'
nivel_actividad = 'moderada'
objetivo = 'perder_grasa'
porcentaje_grasa_actual = 15
porcentaje_grasa_deseado = 10

cbm = calcular_cbm(peso_kg, altura_cm, edad_anos, genero)
aftd = calcular_aftd(cbm, nivel_actividad)
ctn = calcular_ctn(aftd, objetivo)
macronutrientes = calcular_macronutrientes(peso_kg, objetivo)

print(f"CBM: {cbm} calorías")
print(f"AFTD: {aftd} calorías")
print(f"CTN: {ctn} calorías")
print(f"Macronutrientes: Proteínas: {macronutrientes['proteinas']}g, Carbohidratos: {macronutrientes['carbohidratos']}g, Grasas: {macronutrientes['grasas']}g")

# Simulación de ajuste semanal
peso_perdido_semana = 0.5  # Peso perdido en la primera semana
ctn_ajustada = ajustar_calorías_semanalmente(ctn, peso_perdido_semana)
print(f"Nuevas CTN después de ajuste semanal: {ctn_ajustada} calorías")
