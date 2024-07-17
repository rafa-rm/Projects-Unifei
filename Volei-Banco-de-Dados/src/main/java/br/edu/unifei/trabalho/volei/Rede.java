package br.edu.unifei.trabalho.volei;

import javax.persistence.Entity;

import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(callSuper = false)
@Entity
public class Rede extends Posicionamento {
	private static final long serialVersionUID = 7368702321034557548L;

	@Override
	public void realizaAcao() {
		System.out.println("Estou no ataque " + getPosicaoRotacao().name().toLowerCase());
	}
}
