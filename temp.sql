CREATE OR REPLACE PROCEDURE pudt2pedid () 
RETURNS TRIGGER AS $$
BEGIN
	update public.pedido
	set precototal =
	(select ppsum from vprecoproduto
	where vppid = '00000000-5555-7777-1dcd-300020001001'
	)
	where id  = '00000000-5555-7777-1dcd-300020001001'
	;
    RETURN NEW;
END;
$$ 
LANGUAGE plpgsql;


--INSERT INTO public.pedido (id, usuarioid) VALUES('00000000-5555-7777-1dcd-300022001000'::uuid, 1);
'00000000-5555-7777-1dcd-300022001000'

--delete from 
--ins2orders 
/* vprecoproduto
select pp.pedidoid_fk vppid, sum (pp.quantidade * pp.preçounidade ) as ppsum
from pedido_produtos pp 
group by pp.pedidoid_fk 
;

CREATE OR replace trigger trgins2orders after insert on public.pedido_produtos 

REFERENCING NEW TABLE AS inserted
FOR EACH row
EXECUTE FUNCTION check_transfer_balances_to_zero();


CREATE OR REPLACE FUNCTION ins2orders () 
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO public.orders ("userid", "valorproduto")
        VALUES (NEW.quantidade, NEW.precounidade);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_pedido_produtos_insert
AFTER INSERT ON public.pedido_produtos
FOR EACH ROW
EXECUTE PROCEDURE ins2pedid();

--

CREATE OR REPLACE FUNCTION ins2pedid () 
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO public.orders ("userid", "valorproduto")
        VALUES (NEW.quantidade, NEW.precounidade);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_pedido_produtos_update
AFTER INSERT ON public.pedido_produtos
FOR EACH ROW
EXECUTE PROCEDURE ins2pedid();

--

CREATE TRIGGER updt_log
  AFTER UPDATE
  ON public.pedido_produtos
  FOR EACH ROW
  EXECUTE PROCEDURE udt2pedid();

CREATE OR REPLACE FUNCTION udt2pedid () 
RETURNS TRIGGER AS $$
BEGIN
	update public.pedido
	set precototal =
	(select ppsum from vprecoproduto
	where vppid = NEW.pedidoid_fk
	);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;







CREATE OR REPLACE FUNCTION udt2pedid()
  RETURNS trigger AS
$$
BEGIN
INSERT into stu_log VALUES (user, CONCAT('Update Student Record ',
         OLD.NAME,' Class :',OLD.ST_CLASS,' -> Deleted on ',
         NOW()));
RETURN NEW;
END;

$$
LANGUAGE 'plpgsql';

CREATE TRIGGER trigger_pedido_produtos_update
AFTER UPDATE ON public.pedido_produtos
FOR EACH ROW
EXECUTE PROCEDURE udt2pedid();

CREATE TRIGGER trigger_pedido_produtos_update
 BEFORE UPDATE
 ON public.pedido_produtos
 FOR EACH ROW
EXECUTE PROCEDURE udt2pedid();




*/


